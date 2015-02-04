#!/usr/bin/env python3
import vkontakte
import sys
from settings import Settings

def _(s): return s

APP_ID = 4755710

file_name, dot, extension = sys.argv[0].rpartition('.')
if extension == 'py' and file_name != '':
	settings = Settings(file_name + '.conf')
else: settings = Settings(sys.argv[0])

if hasattr(settings, 'access_token'):
	vkapi = vkontakte.api(APP_ID, access_token=settings.access_token)
else:
	login = input(_("Логин:  "))
	passw = input(_("Пароль: "))
	try: vkapi = vkontakte.api(APP_ID, login, passw, scope='messages')
	# I discovered that vk library stores the password
	finally: del passw, vkapi.user_password
	settings.access_token = vkapi.access_token

user = vkapi.users.get(fields='online')[0]
print(_("Здравствуйте, {fname} {lname}!").format(fname=user.first_name, lname=user.last_name), end=' ')
print("O" if user.online else "Ø")

dialogs = vkapi.messages.getDialogs(count=10, preview_length=80).items
for i, diag in enumerate(dialogs, start=1):
	unread = diag.unread if 'unread' in diag else 0
	if unread >= 1000: unread = "..."
	if 'chat_id' in diag.message: title = diag.message.title
	else:
		sender = vkapi.users.get(user_ids=diag.message.user_id)[0]
		title = _("{fname} {lname}").format(fname=sender.first_name, lname=sender.last_name)

	print("{0:>3}".format(i), "{0:>3}".format(unread), "{0:<85}".format(title))
	print(" "*13, "{0:<80}".format(diag.message.body))

diag_num = int(input(_("№ диалога: "))) - 1
diag = dialogs[diag_num]
if 'chat_id' in diag.message: us_id, ch_id = 0, diag.message.chat_id
else: ch_id, us_id = 0, diag.message.user_id
messages = vkapi.messages.getHistory(chat_id=ch_id, user_id=us_id).items
for msg in messages[::-1]:
	align = '>' if msg.out else '<'
	print(" "*13, "{0:{1}80}".format(msg.body, align))
