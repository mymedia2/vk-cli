#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
	name = "vk-cli",
	version = "0.01",
	description = "Vkontakte (vk.com) messenger with CLI for geeks",
	url = "https://github.com/mymedia2/vk-cli",
	author = "Nicholas Guriev",
	author_email = "guriev-ns@ya.ru",
	license = "LGPLv3",
	packages = find_packages(),
	install_requires = [
		"vk"
	],
	keywords = "vk.com vk cli",
	entry_points = {
		"console_scripts": [ "vk-cli = vk_cli:app", ],
	},
)
