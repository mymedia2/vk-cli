#!/usr/bin/env python3
import argparse
from dialogs import Dialogs
from hub import Hub
from messages import Messages
from sender import Sender

def get_args():
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest="action")

	dialogs_parser = subparsers.add_parser("dialogs")
	dialogs_parser.add_argument("--page", type=int, default=0)

	show_parser = subparsers.add_parser("show")
	show_parser.add_argument("--id", type=int)
	show_parser.add_argument("--chat", type=int)
	show_parser.add_argument("--page", type=int, default=0)

	send_parser = subparsers.add_parser("send")
	send_parser.add_argument("--id", type=int)
	send_parser.add_argument("--chat", type=int)
	send_parser.add_argument("text", type=str)

	return parser.parse_args()

def app():
	Hub()	# инициализируем одиночку
	args = get_args()
	if args.action == None or args.action == "dialogs":
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
