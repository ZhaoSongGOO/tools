#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright by zhaosonggo in 2024, All Rights Reserved.


from core.plugin import Plugin
from core.change_list import ChangeList
from plugins.code_format.formater import FormaterFactory
import os


class CodeFormatPlugin(Plugin):
    def __init__(self):
        super().__init__("code-format")

    def help(self):
        return "format code style by google-style."

    def accept(self, args):
        change_list = ChangeList()
        files = []
        if args.all:
            files = change_list.get_all_files_from_root(os.getcwd())
        else:
            files = change_list.get_changed_files()
        formater_queue = []
        for file in files:
            formater = FormaterFactory(file)
            if formater is not None:
                formater_queue.append(formater)
        for formater in formater_queue:
            formater.format()

    def build_command_args(self, subparser):
        subparser.add_argument("--all", action="store_true", help="Format all files")
        subparser.add_argument(
            "-v", "--verbose", action="store_true", help="Enable verbose mode"
        )
