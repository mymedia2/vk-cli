#!/usr/bin/env python3
import sys
from dialogs import Dialogs
from hub import Hub
from messages import Messages
from sender import Sender

def app():
	Hub()	# инициализируем одиночку
	if len(sys.argv) == 1:
		Dialogs().call()
	elif sys.argv[1] == "show":
		Messages().call()
	elif sys.argv[1] == "send":
		Sender().call()

if __name__ == "__main__": app()
