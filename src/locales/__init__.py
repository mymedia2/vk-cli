import configparser
import os, sys
_translation = None
def _(category, string):
	global _translation
	if not _translation:
		_translation = configparser.ConfigParser()
		_translation.read(os.path.dirname(sys.argv[0]) + "/locales/ru.ini")
	return _translation[category][string]
