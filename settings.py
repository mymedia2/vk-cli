#!/usr/bin/env python3
class Settings:
	def __init__(self, file_name, default_settings={}):
		self._file_name = file_name
		try:
			f = open(self._file_name, 'r')
# TODO: replace eval with something more secure
			self.__dict__.update(eval(f.read()))
			f.close()
		except (IOError, SyntaxError):
			self.__dict__.update(default_settings)

	def __setattr__(self, key, value):
		self.__dict__[key] = value
		if not key.startswith('_'):
			f = open(self._file_name, 'w')
			f.write(repr(self.__dict__))
			f.close()
