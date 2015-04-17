import sys
import vkontakte
from console import Console
from settings import Settings
from user import User, UserPack

class Hub(object):
	"""	Концентратор всех объектов, которые я являются общими для программы"""

	def __init__(self):
		"""	Инициализирует:
			self.settings
			self.vkapi
			self.current_user
			self.users
		"""
		file_name, dot, extension = sys.argv[0].rpartition('.')
		if extension == 'py' and file_name != '':
			self.settings = Settings(file_name + '.conf')
		else: self.settings = Settings(sys.argv[0])

		APP_ID = 4755710
		if hasattr(self.settings, 'access_token'):
			self.vkapi = vkontakte.api(APP_ID, access_token=self.settings.access_token)
		else:
			# TODO: реализовать запрос через Interact
			login = input(_("Логин:  "))
			passw = input(_("Пароль: "))
			try: self.vkapi = vkontakte.api(APP_ID, login, passw, scope='messages')
			# я обнаружил, что библиотека храинт пароль
			finally: del passw, self.vkapi.user_password
			settings.access_token = vkapi.access_token

		self.current_user = User(0)
		self.users = UserPack([self.current_user])

		self.console = Console()
