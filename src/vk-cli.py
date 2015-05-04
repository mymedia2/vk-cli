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

	show_parser = subparsers.add_parser("show")
	show_parser.add_argument("--id", type=int)
	show_parser.add_argument("--chat", type=int)

	send_parser = subparsers.add_parser("send")

	return parser.parse_args()

def app():
	Hub()	# инициализируем одиночку
	args = get_args()
	if args.action == None or args.action == "dialogs":
		Dialogs().call()
	elif args.action == "show":
		if args.id and not args.chat:
			Messages().call(user_id=args.id)
		elif not args.id and args.chat:
			Messages().call(chat_id=args.chat)
		else: raise ValueError
	elif args.action == "send":
		Sender().call()

if __name__ == "__main__": app()
