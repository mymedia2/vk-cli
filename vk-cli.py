#!/usr/bin/env python3
import vk
from settings import Settings

def _(s): return s

settings = Settings('vk-cli.conf')
vkapi = vk.API(4755710, settings.login, settings.password, scope='messages')
user = vkapi.users.get(fields='online')[0]
print(_("Здравствуйте, {fname} {lname}!").format(fname=user['first_name'], lname=user['last_name']), end=' ')
print("O" if user['online'] else "Ø")
dialogs = vkapi.messages.getDialogs(count=10, preview_length=80)['items']
for i, diag in enumerate(dialogs, start=1):
	unread = diag['unread'] if 'unread' in diag else 0
	if unread >= 1000: unread = "..."
	if 'chat_id' in diag['message']: title = diag['message']['title']
	else:
		sender = vkapi.users.get(user_ids=diag['message']['user_id'])[0]
		title = _("{fname} {lname}").format(fname=sender['first_name'], lname=sender['last_name'])

	print("{0:>3}".format(i), "{0:>3}".format(unread), "{0:<85}".format(title))
	print(" "*13, "{0:<80}".format(diag['message']['body']))
