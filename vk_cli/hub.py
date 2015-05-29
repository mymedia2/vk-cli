#!/usr/bin/env python3

import os, sys
import vk_cli.vkontakte
from vk_cli.console import Console
from vk_cli.settings import Settings
from vk_cli.singleton import singleton
from vk_cli.user import User, UserPack

@singleton
class Hub(object):
	"""Концентратор всех объектов, которые являются общими для программы"""

	#: API ВКонтакте, осуществляет работу с сетью, экземпляр vkontakte.api
	vkapi = None

	#: Настройки всей программы, осущесвляет запись в файл, экземпляр Settings
	settings = None

	#: Объект User текущего пользователя
	current_user = None

	#: UserPack со всеми закешированными пользователями
	users = None

	#: экземпляр Console для ввода-вывода
	console = None

	def __init__(self):
		settings_file_name = "." + os.path.basename(sys.argv[0]) + ".conf"
		self.settings = Settings(os.path.expanduser(os.path.join("~", settings_file_name)))

		APP_ID = 4755710
		if hasattr(self.settings, 'access_token'):
			self.vkapi = vk_cli.vkontakte.api(APP_ID, access_token=self.settings.access_token)
		else:
			# TODO: реализовать запрос через Interact
			login = input("Логин: ")
			passw = input("Пароль: ")
			try: self.vkapi = vk_cli.vkontakte.api(APP_ID, login, passw, scope='messages')
			# я обнаружил, что библиотека храинт пароль
			finally: del passw, self.vkapi.user_password
			self.settings.access_token = self.vkapi.access_token

		self.current_user = User(0)
		self.users = UserPack([self.current_user])

		self.console = Console()
