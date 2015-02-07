#!/usr/bin/env python3
import vkontakte
class User(object):
	def __init__(self, id):
		self.id = id
	def __hash__(self):
		return self.id
	def header(self):
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
	def __init__(self, arg=None):
		super().__init__()
		if arg is not None: self.add(arg)
	def __iter__(self):
		return iter(self.values())
	def add(self, arg):
		if hasattr(arg, '__iter__'):
			for elem in arg: self.add(elem)
		else:
			if type(arg) is User: self[arg.id] = arg
			else: self[arg] = User(arg)

	def fill_all(self, fields=""):
		vkapi = vkontakte.api()
		ids = ",".join((str(u.id) for u in self))
		response = vkapi.users.get(user_ids=ids, fields=fields)
		self.clear()
		for elem in response:
			user = User(elem.id)
			user.__dict__ = elem
			self.add(user)
