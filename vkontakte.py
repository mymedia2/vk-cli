#!/usr/bin/env python3
import vk
class api(vk.API):
	#Singleton
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, 'instance'):
			cls.instance = super().__new__(cls)
		return cls.instance
	def __init__(self, *args, **kwargs):
		if not hasattr(self.__class__, 'initialised'):
			super().__init__(*args, **kwargs)
			self.__class__.initialised = True
	def __call__(self, *args, **kwargs):
		return FieldDict.process_all(super().__call__(*args, **kwargs))

class FieldDict(dict):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__dict__ = self
	@classmethod
	def process_all(cls, response):
		if type(response) is dict:
			for key, elem in response.items():
				response[key] = cls.process_all(elem)
			return cls(response)
		if type(response) is list:
			for i, elem in enumerate(response):
				response[i] = cls.process_all(elem)
		return response
