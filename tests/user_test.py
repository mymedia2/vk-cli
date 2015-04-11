#!/usr/bin/env python3
from user import User, UserPack
from settings import Settings
import unittest, vkontakte
APP_ID = 4755710
MY_ID = 147603034

class UserTest(unittest.TestCase):
	def test1_compare(self):
		durov = User(1)
		me = User(MY_ID)
		twin = User(MY_ID)
		self.assertFalse(me is twin)
		self.assertTrue(me == twin)
		self.assertFalse(me == durov)
		self.assertFalse(me != twin)
		self.assertTrue(me != durov)

class UserPackTest(unittest.TestCase):
	def test1_init(self):
		users = UserPack([1, MY_ID])
		iterator = iter(users)
		first = next(iterator)
		if first == User(1): self.assertEqual(next(iterator), User(MY_ID))
		else:
			self.assertEqual(first, User(MY_ID))
			self.assertEqual(next(iterator), User(1))
		with self.assertRaises(StopIteration): next(iterator)
		s = set()
		for u in users: s.add(u)
		self.assertEqual(s - {User(1), User(MY_ID)}, set())
	def test2_addition(self):
		users = UserPack()
		users.add(1)
		users.add([User(MY_ID)])
		self.assertEqual(users, UserPack([User(1), MY_ID]))

class UserPackTestNetwork(unittest.TestCase):
	durov = User(1)
	me = User(MY_ID)
	def setUpClass():
		settings = Settings("vk-cli.conf")
		vkontakte.api(APP_ID, access_token=settings.access_token)
	def test1_generic(self):
		both = UserPack((self.durov, self.me))
		both.fill_all()
		both = list(both)
		both = {both[0].id: both[0], both[1].id: both[1]}
		self.assertEqual(" ".join((both[1].first_name, both[1].last_name)), "Павел Дуров")
		self.assertEqual(" ".join((both[MY_ID].first_name, both[MY_ID].last_name)), "Коля Гурьев")
	def test2_fields(self):
		both = UserPack((self.durov, self.me))
		both.fill_all("city,country")
		both = list(both)
		both = {both[0].id: both[0], both[1].id: both[1]}
		self.assertEqual(both[1].city.id, 2)
		self.assertEqual(both[MY_ID].city.id, 1)
		self.assertTrue(both[1].country.title == both[MY_ID].country.title == "Россия")
	def tearDownClass():
		cl = vkontakte.api().__class__
		del cl.initialised, cl.instance
