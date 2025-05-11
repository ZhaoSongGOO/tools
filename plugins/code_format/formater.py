#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright by zhaosonggo in 2024, All Rights Reserved.

import subprocess
from core.log import Log


class Formater:
    def __init__(self, cmd, input):
        self.cmd = cmd
        self.input = input

    def format(self):
        Log.info(f"Formatting {self.input}")
        subprocess.check_call(
            self.cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
        )


class CFormater(Formater):
    def __init__(self, file):
        super().__init__(f"clang-format -style=google -i {file}", file)


class GnFormater(Formater):
    def __init__(self, file):
        super().__init__(f"gn format {file}", file)


class PyFormater(Formater):
    def __init__(self, file):
        super().__init__(f"black {file}", file)


def FormaterFactory(file: str):
    if (
        file.endswith(".c")
        or file.endswith(".cc")
        or file.endswith(".cpp")
        or file.endswith(".h")
    ):
        return CFormater(file)
    elif file.endswith(".gn"):
        return GnFormater(file)
    elif file.endswith(".py"):
        return PyFormater(file)
    else:
        return None
