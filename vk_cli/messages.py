#!/usr/bin/env python3

from vk_cli.feature_interface import FeatureInterface
from os import get_terminal_size

class Messages(FeatureInterface):
	"""Отвечает за работу экрана с сообщениями из конкретного диалога"""

	def get_data(self, chat_id=0, user_id=0, page=0):
		params = { "chat_id": chat_id, "user_id": user_id, "offset": page * 20 }
		messages = self.common.vkapi.messages.getHistory(**params).items

		if len(messages) and 'chat_id' in messages[0]:
			# если в диалоге есть сообщения и этот диалог является беседой
			for msg in messages:
				self.common.users.add(msg.from_id)
			self.common.users.fill_all("online")

		return messages

	def render(self, messages):
		last_msg_author = None
		msg_readed = list()
		column_width = get_terminal_size().columns
		for msg in messages[::-1]:
			# печаем имя пользователя, если мы в беседе и это входящее сообщение
			# дважды подряд имя пользователя не печатаем
			if not msg.out and 'chat_id' in msg and last_msg_author != msg.from_id:
				last_msg_author = msg.from_id
				self.common.console.write(self.common.users[msg.from_id].header())

			align = '>' if msg.out else '<'
			for line in msg.body.split('\n'):
				self.common.console.write(" "*5, "{0:{1}{2}}".format(line, align, column_width - 10))

			# запоминаем ID's сообщ. которые входящие и не прочитаные
			if not msg.out and not msg.read_state:
				msg_readed.append(str(msg.id))

		if msg_readed:
			self.common.vkapi.messages.markAsRead(message_ids=','.join(msg_readed))
