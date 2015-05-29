#!/usr/bin/env python3

class Settings:
	"""Сохраняет настройки программы."""

	def __init__(self, file_name, default_settings={}):
		"""Загружает настройки из file_name.

		Если эта попытка терпит неудачу, например, при первом запуске
		программы, когда такого файла нет, то используются default_settings
		"""
		self._file_name = file_name
		try:
			f = open(self._file_name, 'r')
			# TODO: заменить eval чем-нибудь более безопасным
			self.__dict__.update(eval(f.read()))
			f.close()
		except (IOError, SyntaxError):
			self.__dict__.update(default_settings)

	def __setattr__(self, key, value):
		"""Сохраняет все настройки в файле file_name. См. __init__"""
		self.__dict__[key] = value
		# TODO: запретить запись служебных значений
		if not key.startswith('_'):
			f = open(self._file_name, 'w')
			f.write(repr(self.__dict__))
			f.close()
