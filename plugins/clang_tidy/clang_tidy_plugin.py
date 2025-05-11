#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

# Copyright by zhaosonggo in 2024, All Rights Reserved.


from core.plugin import Plugin
from core.change_list import ChangeList
import os
from tqdm import tqdm


def filter_source_file(files):
    result = []
    for file in files:
        if (
            file.endswith(".c")
            or file.endswith(".cc")
            or file.endswith(".cpp")
            or file.endswith(".h")
        ):
            result.append(file)
    return result


class ClangTidyPlugin(Plugin):
    def __init__(self):
        super().__init__("clang-tidy")
        self.log_file = "clang-tidy-report.report"

    def help(self):
        return "static check by clang-tidy."

    def accept(self, args):
        change_list = ChangeList()
        if args.all:
            files = change_list.get_all_files_from_root(os.getcwd())
        else:
            files = change_list.get_changed_files()
        files = filter_source_file(files)
        report = open(self.log_file, "w")
        for file in files:
            try:
                subprocess.check_call(
                    f"clang-tidy -p {args.compile_commands_path} {file}",
                    shell=True,
                    stdout=report,
                    stderr=report,
                )
            except Exception as e:
                print(e, "You can view detailed information in the report")

    def build_command_args(self, subparser):
        subparser.add_argument("-ccp", "--compile_commands_path", required=True)
        subparser.add_argument("--all", action="store_true", help="Format all files")
        subparser.add_argument(
            "-v", "--verbose", action="store_true", help="Enable verbose mode"
        )
