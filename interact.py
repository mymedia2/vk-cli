from hub import Hub

class Interact(object):

	#: Ссылка на общий Hub, изпользуется чтобы считывать команды с консоли
	share = None

	def __init__(self):
		self.share = Hub()
