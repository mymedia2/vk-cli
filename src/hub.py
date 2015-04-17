#!/usr/bin/python3
import sys
import vkontakte
from console import Console
from settings import Settings
from singleton import singleton
from user import User, UserPack

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
		file_name, dot, extension = sys.argv[0].rpartition('.')
		if extension == 'py' and file_name != '':
			self.settings = Settings(file_name + '.conf')
		else: self.settings = Settings(sys.argv[0])

		APP_ID = 4755710
		if hasattr(self.settings, 'access_token'):
			self.vkapi = vkontakte.api(APP_ID, access_token=self.settings.access_token)
		else:
			# TODO: реализовать запрос через Interact
			login = input("Логин: ")
			passw = input("Пароль: ")
			try: self.vkapi = vkontakte.api(APP_ID, login, passw, scope='messages')
			# я обнаружил, что библиотека храинт пароль
			finally: del passw, self.vkapi.user_password
			settings.access_token = vkapi.access_token

		self.current_user = User(0)
		self.users = UserPack([self.current_user])

		self.console = Console()
