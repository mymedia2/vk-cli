#!/usr/bin/env python3

from vk_cli.hub import Hub

class Interact(object):

	#: Ссылка на общий Hub, изпользуется чтобы считывать команды с консоли
	common = None

	def __init__(self):
		self.common = Hub()
