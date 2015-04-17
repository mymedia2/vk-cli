from feature_interface import FeatureInterface

class Dialogs(FeatureInterface):
	"""Отвечает за работу экрана со списком диалогов пользователя"""

	def get_data(self):
		dialogs = self.share.vkapi.messages.getDialogs(count=10, preview_length=80).items
		for diag in dialogs:
			if 'chat_id' not in diag.message:
				self.share.users.add(diag.message.user_id)
		self.share.users.fill_all("online")
		return dialogs

	def render(self, dialogs):
		#TODO: запихнать dialogs в именнованный кортеж
		for i, diag in enumerate(dialogs, start=1):
			unread = diag.unread if 'unread' in diag else 0
			if unread >= 1000: unread = "..."
			if 'chat_id' in diag.message: title = diag.message.title
			else: title = self.share.users[diag.message.user_id].header()

			out = self.share.console.write
			out("{0:>3}".format(i), "{0:>3}".format(unread), "{0:<85}".format(title))
			out(" "*13, "{0:<80}".format(diag.message.body))
