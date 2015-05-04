from feature_interface import FeatureInterface

class Sender(FeatureInterface):
	def call(self, text_message, user_id=0, chat_id=0):
		self.common.vkapi.messages.send(user_id=user_id, chat_id=chat_id, message=text_message)
