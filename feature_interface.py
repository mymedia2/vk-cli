#!/usr/bin/python3
from hub import Hub

class FeatureInterface(object):
	"""Является интерфейсом для каждой из возможности программы"""

	#: Ссылка на общий Hub, изпользуется возможностями для доступа к API
	share = None

	def __init__(self):
		self.share = Hub()
	
	def get_data(self):
		"""Возвращает словарь с данными, которые можно отрисовывать на консоли.

		Сами данные могут быть получены из интернета."""
		raise NotImplementedError
	
	def render(self, data):
		"""Отрисовывает словарь data в self.share.console"""
		raise NotImplementedError
	
	def call(self):
		"""Обеспечивает лёкгий вызов возможности"""
		return self.render(self.get_data())
