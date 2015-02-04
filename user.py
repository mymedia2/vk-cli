#!/usr/bin/env python3
import vkontakte
class User(object):
	def __init__(self, id):
		self.id = id
	def __hash__(self):
		return self.id
class UserPack(set):
	def fill_all(self, fields=""):
		vkapi = vkontakte.api()
		ids = ",".join((str(u.id) for u in self))
		response = vkapi.users.get(user_ids=ids, fields=fields)
		self.clear()
		for elem in response:
			user = User(elem.id)
			user.__dict__ = elem
			self.add(user)
