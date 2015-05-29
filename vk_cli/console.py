#!/usr/bin/env python3

class Console(object):
	"""Взаимодействует с файлами ввода-вывода.

	Любое взаимодействие с пользователём осуществляется через этот класс.
	"""

	def write(self, *args):
		"""Печатает форматированную строчку.

		TODO: здесь появится описание синтаксиса формата.
		"""
		return print(*args)

	def read(self, format):
		return input(format)
