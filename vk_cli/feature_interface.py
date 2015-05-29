#!/usr/bin/env python3

from vk_cli.hub import Hub

class FeatureInterface(object):
	"""Является интерфейсом для каждой из возможности программы"""

	#: Ссылка на общий Hub, может изпользоваться возможностями для доступа к API
	common = None

	def __init__(self):
		self.common = Hub()
	
	def get_data(self, *args, **kwargs):
		"""Возвращает словарь с данными, которые можно отрисовывать на консоли.

		Сами данные могут быть получены из интернета.
		Необязательно принимать любое количесво аргументов, можно
		переопределить свои.
		"""
		raise NotImplementedError
	
	def render(self, data):
		"""Отрисовывает словарь data в self.common.console"""
		raise NotImplementedError
	
	def call(self, *args, **kwargs):
		"""Обеспечивает лёкгий вызов возможности"""
		return self.render(self.get_data(*args, **kwargs))
