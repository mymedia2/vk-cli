#!/usr/bin/env python3
import vk
from settings import Settings

def _(s):
	return s

settings = Settings('vk-cli.conf')
vkapi = vk.API(4755710, settings.login, settings.password, scope='messages')
user = vkapi.users.get(fields='online')[0]
print(_("Вы %s %s. %s") % (user['first_name'], user['last_name'], "Online" if user['online'] else "Offline"))
message = vkapi.messages.get(out=1, count=1)['items'][0]
print(_("Ваше последнее сообщение:\n%s") % (message['body']))
