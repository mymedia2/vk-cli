#!/usr/bin/env python3
from user import User, UserPack
from settings import Settings
import unittest, vkontakte
APP_ID = 4755710
MY_ID = 147603034
def setUpModule():
	settings = Settings("vk-cli.conf")
	vkontakte.api(APP_ID, access_token=settings.access_token)
class UserPackTest(unittest.TestCase):
	durov = User(1)
	me = User(MY_ID)
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
		self.assertEqual(" ".join((both[1].first_name, both[1].last_name)), "Павел Дуров")
		self.assertEqual(" ".join((both[MY_ID].first_name, both[MY_ID].last_name)), "Коля Гурьев")
		self.assertTrue(both[1].country.title == both[MY_ID].country.title == "Россия")
def tearDownModule():
	cl = vkontakte.api().__class__
	del cl.initialised, cl.instance
