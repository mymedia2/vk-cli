from vkontakte import FieldDict
import unittest

class FieldDictTest(unittest.TestCase):
	def test1(self):
		fd = FieldDict.process_all({'a': 1, 'b': 2, 'c': "foo", 'd': "bar"})
		self.assertEqual(fd.a, 1)
		self.assertEqual(fd['a'], 1)
		self.assertEqual(fd.b, 2)
		self.assertEqual(fd['b'], 2)
		self.assertEqual(fd.c, "foo")
		self.assertEqual(fd['c'], "foo")
		self.assertEqual(fd.d, "bar")
		self.assertEqual(fd['d'], "bar")
	def test2(self):
		fd = FieldDict.process_all([42, "foo", {'c': 15, 'd': ["bar"]}])
		self.assertEqual(fd[0], 42)
		self.assertEqual(fd[1], "foo")
		self.assertEqual(fd[2].c, 15)
		self.assertEqual(fd[2].d[0], "bar")
	def test3(self):
		fd = FieldDict.process_all(10)
		self.assertEqual(fd, 10)
	def test4(self):
		fd = FieldDict.process_all({})
		self.assertEqual(len(fd), 0)
		with self.assertRaises(AttributeError):
			fd.some
	def test5(self):
		fd = FieldDict.process_all([])
		self.assertEqual(len(fd), 0)
		with self.assertRaises(AttributeError):
			fd.some

if __name__ == "__main__":
	unittest.main()
