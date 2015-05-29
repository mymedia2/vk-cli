#!/usr/bin/env python3

import argparse
import vk_cli.locales
from vk_cli.dialogs import Dialogs
from vk_cli.hub import Hub
from vk_cli.messages import Messages
from vk_cli.sender import Sender

def get_args():
	# TODO: запихнуть этого монстра в отдельный файл и в класс-обёртку
	parser = argparse.ArgumentParser(description=_("help", "program_description"), add_help=False)

	parent_group = parser.add_argument_group(title=_("help", "parametrs_title"))
	parent_group.add_argument("-h", "--help", action="help", help=_("help", "help_key_all_desciption"))

	subparsers = parser.add_subparsers(dest="action", title=_("help", "action_title"))

	dialogs_parser = subparsers.add_parser("dialogs", help=_("help", "dialogs_title"), add_help=False)
	dialogs_group = dialogs_parser.add_argument_group(title=_("help", "parametrs_title"))
	dialogs_group.add_argument("-p", "--page", type=int, default=0, help=_("help", "page_key_description"), metavar="INT")
	dialogs_group.add_argument("-h", "--help", action="help", help=_("help", "help_key_command_description"))

	show_parser = subparsers.add_parser("show", help=_("help", "show_title"), add_help=False)
	show_group = show_parser.add_argument_group(title=_("help", "parametrs_title"))
	show_group.add_argument("-p", "--page", type=int, default=0, help=_("help", "page_key_description"), metavar="INT")
	show_group.add_argument("--id", type=int, metavar="USER_ID")
	show_group.add_argument("--chat", type=int, metavar="CHAT_ID")
	show_group.add_argument("-h", "--help", action="help", help=_("help", "help_key_command_description"))

	send_parser = subparsers.add_parser("send", help=_("help", "send_title"), add_help=False)
	send_group = send_parser.add_argument_group(title=_("help", "parametrs_title"))
	send_group.add_argument("text", type=str, help=_("help", "text_key_desciption"))
	send_group.add_argument("--id", type=int, metavar="USER_ID")
	send_group.add_argument("--chat", type=int, metavar="CHAT_ID")
	send_group.add_argument("-h", "--help", action="help", help=_("help", "help_key_command_description"))

	return parser.parse_args()

def app():
	args = get_args()
	Hub()	# инициализируем одиночку
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
