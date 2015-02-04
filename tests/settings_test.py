#!/usr/bin/env python3
from settings import Settings
import unittest, sys, os
class SettingsTest(unittest.TestCase):
	file_name = sys.argv[0]+".conf"
	def test1(self):
		s1 = Settings(self.file_name)
		s1.a = "foo"
		s1.b = "bar"
		s1.c = 42
		s2 = Settings(self.file_name)
		self.assertEqual(s2.a, "foo")
		self.assertEqual(s2.b, "bar")
		self.assertEqual(s2.c, 42)
	def test2(self):
		s = Settings(self.file_name, {'a': "foo", 'b': "bar", 'c': 42})
		self.assertEqual(s.a, "foo")
		self.assertEqual(s.b, "bar")
		self.assertEqual(s.c, 42)
	def tearDown(self):
		try: os.remove(self.file_name)
		except: pass

if __name__ == "__main__":
	unittest.main()
