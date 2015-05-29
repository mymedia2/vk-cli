#!/usr/bin/env python3

import vk_cli.vkontakte

class User(object):
	"""Представляет пользователя ВКонтакте."""

	def __init__(self, id):
		self.id = int(id)

	def __hash__(self):
		return self.id

	def __eq__(self, other):
		return self.id == other.id

	def __ne__(self, other):
		return not(self == other)

	def header(self):
		"""Возвращает имя и фамилию пользователя.

		Также, если пользователь онлайн или заблокирован, приписывает
		соответсвующий значок.
		"""
		l = [self.first_name, self.last_name]
		if hasattr(self, 'deactivated'):
			if self.deactivated == "deleted": l.append("X")
			elif self.deactivated == "banned": l.append("x")
		elif hasattr(self, 'online'):
			if self.online:
				if hasattr(self, 'online_mobile') and self.online_mobile:
					l.append("o")
				else: l.append("O")
			else: l.append("Ø")
		return " ".join(l)


class UserPack(dict):
	"""Набор пользователей ВКонтакте.

	Необходим для пакетной загрузки информации о пользователях с помощью
	метода fill_all.
	"""

	def __init__(self, arg=None):
		super().__init__()
		if arg is not None: self.add(arg)

	def __iter__(self):
		return iter(self.values())

	def add(self, user):
		"""Добавляет ещё одного пользователя в набор.

		Если параметр — контейнер, то все его элементы рекурсивно
		добавляются в набор. Аргумент может быть как экземпляром типа User,
		так и обычной строкой или числом, содержащей ID пользователя ВКонтакте.
		"""
		u = user
		if hasattr(u, '__iter__'):
			for elem in u: self.add(elem)
		else:
			if type(u) is User: self[u.id] = u
			else: self[int(u)] = User(u)

	def fill_all(self, fields=""):
		"""Заполняет указанные поля для всех содержащися пользователей.

		Выполняет запрос через интернет.
		"""
		vkapi = vkontakte.api()
		ids = ",".join((str(u.id) for u in self))
		response = vkapi.users.get(user_ids=ids, fields=fields)
		self.clear()
		for elem in response:
			user = User(elem.id)
			user.__dict__ = elem
			self.add(user)
