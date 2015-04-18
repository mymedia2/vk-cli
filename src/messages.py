from feature_interface import FeatureInterface

class Messages(FeatureInterface):
	"""Отвечает за работу экрана с сообщениями из конкретного диалога"""

	def get_data(self, chat_id=0, user_id=0):
		return self.common.vkapi.messages.getHistory(chat_id=chat_id, user_id=user_id).items

	def render(self, messages):
		for msg in messages[::-1]:
			align = '>' if msg.out else '<'
			for line in msg.body.split('\n'):
				self.common.console.write(" "*13, "{0:{1}80}".format(line, align))
