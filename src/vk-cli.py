#!/usr/bin/env python3
import argparse
from dialogs import Dialogs
from hub import Hub
from messages import Messages
from sender import Sender

def get_args():
	# TODO: запихнуть этого монстра в отдельный файл и в класс-обёртку
	parser = argparse.ArgumentParser(description="Мессенджер ВКонтаке с CLI для гиков", add_help=False)

	parent_group = parser.add_argument_group(title="Параметры")
	parent_group.add_argument("-h", "--help", action="help", help="Показать эту справку и выйти")

	subparsers = parser.add_subparsers(dest="action", title="Действия")

	dialogs_parser = subparsers.add_parser("dialogs", help="Показть список диалогов текущего пользователя", add_help=False)
	dialogs_group = dialogs_parser.add_argument_group(title="Параметры")
	dialogs_group.add_argument("-p", "--page", type=int, default=0, help="Страница для отображения", metavar="INT")
	dialogs_group.add_argument("-h", "--help", action="help", help="Показать справку об этой команде и выйти")

	show_parser = subparsers.add_parser("show", help="Показать сообщения из определённого диалога", add_help=False)
	show_group = show_parser.add_argument_group(title="Параметры")
	show_group.add_argument("-p", "--page", type=int, default=0, help="Страница для отображения", metavar="INT")
	show_group.add_argument("--id", type=int, metavar="USER_ID")
	show_group.add_argument("--chat", type=int, metavar="CHAT_ID")
	show_group.add_argument("-h", "--help", action="help", help="Показать справку об этой команде и выйти")

	send_parser = subparsers.add_parser("send", help="Отправить сообщение", add_help=False)
	send_group = send_parser.add_argument_group(title="Параметры")
	send_group.add_argument("text", type=str, help="Текст сообщения")
	send_group.add_argument("--id", type=int, metavar="USER_ID")
	send_group.add_argument("--chat", type=int, metavar="CHAT_ID")
	send_group.add_argument("-h", "--help", action="help", help="Показать справку об этой команде и выйти")

	return parser.parse_args()

def app():
	Hub()	# инициализируем одиночку
	args = get_args()
	if args.action == None:
		Dialogs().call()
	elif args.action == "dialogs":
		Dialogs().call(page=args.page)
	elif args.action == "show":
		if args.id and not args.chat:
			Messages().call(user_id=args.id, page=args.page)
		elif not args.id and args.chat:
			Messages().call(chat_id=args.chat, page=args.page)
		else: raise ValueError
	elif args.action == "send":
		if args.id and not args.chat:
			Sender().call(args.text, user_id=args.id)
		elif not args.id and args.chat:
			Sender().call(args.text, chat_id=args.chat)
		else: raise ValueError

if __name__ == "__main__": app()
