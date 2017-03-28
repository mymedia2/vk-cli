#!/usr/bin/env python3

from vk_cli.feature_interface import FeatureInterface
from os import get_terminal_size

class Dialogs(FeatureInterface):
	"""Отвечает за работу экрана со списком диалогов пользователя"""

	#: Сохраняет последний список диалогов, чтобы потом можно было определить,
	#: какой диалог надо показывать, если известен его номер.
	#: Пока не реалиозвано
	last_list = None

	def get_data(self, page=0):
		params = { "count": 10, "preview_length": 80, "offset": page * 10 }
		self.dialogs = self.common.vkapi.messages.getDialogs(**params).items
		for diag in self.dialogs:
			if 'chat_id' not in diag.message:
				self.common.users.add(diag.message.user_id)
		self.common.users.fill_all("online")
		return self.dialogs

	def render(self, dialogs):
		#TODO: запихать dialogs в именнованный кортеж
		column_width = get_terminal_size().columns - 10 # 10 == " "*5
		for i, diag in reversed(list(enumerate(dialogs, start=1))):
			unread = diag.unread if 'unread' in diag else 0
			if unread >= 1000: unread = "..."
			if 'chat_id' in diag.message:
				title = diag.message.title
				id_ = diag.message.chat_id
			else:
				title = self.common.users[diag.message.user_id].header()
				id_ = diag.message.user_id

			out = self.common.console.write
			out("{0:>2}".format(i), "{0:^10}".format(id_),
				"{0:>3}".format(unread), "{0:<{1}}".format(title, column_width - 13))
			out(" "*17, "{0:<{1}}".format(diag.message.body, column_width - 31))
