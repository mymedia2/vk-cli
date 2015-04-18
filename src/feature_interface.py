#!/usr/bin/python3
from hub import Hub

class FeatureInterface(object):
	"""Является интерфейсом для каждой из возможности программы"""

	#: Ссылка на общий Hub, может изпользоваться возможностями для доступа к API
	share = None

	def __init__(self):
		self.share = Hub()
	
	def get_data(self, *args, **kwargs):
		"""Возвращает словарь с данными, которые можно отрисовывать на консоли.

		Сами данные могут быть получены из интернета.
		Необязательно принимать любое количесво аргументов, можно
		переопределить свои.
		"""
		raise NotImplementedError
	
	def render(self, data):
		"""Отрисовывает словарь data в self.share.console"""
		raise NotImplementedError
	
	def call(self, *args, **kwargs):
		"""Обеспечивает лёкгий вызов возможности"""
		return self.render(self.get_data(*args, **kwargs))
