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

	send_parser = subparsers.add_parser("send")

	return parser.parse_args()

def app():
	Hub()	# инициализируем одиночку
	args = get_args()
	if args.action == None or args.action == "dialogs":
		Dialogs().call()
	elif args.action == "show":
		Messages().call(args.id)
	elif args.action == "send":
		Sender().call()

if __name__ == "__main__": app()
