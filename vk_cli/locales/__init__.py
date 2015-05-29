import builtins
import configparser
import os, sys

_translation_file = None

def translate(category, string):
	"""Возвращает переведённую строчку из заданой категории.

	При первом вызове также читается соответствующий ini файл с переводами.
	В глобальное пространство имён импортируется "_" - синоним для этой функции.
	"""

	global _translation_file
	if not _translation_file:
		language_name = os.getenv("LANG")[:2]
		ini_file = language_name + ".ini.py"
		if not os.path.isfile(os.path.join(os.path.dirname(__file__), ini_file)):
			ini_file = "ru.ini.py"
		_translation_file = configparser.ConfigParser()
		_translation_file.read(os.path.join(os.path.dirname(__file__), ini_file))
	return _translation_file[category][string]

builtins.__dict__["_"] = translate
