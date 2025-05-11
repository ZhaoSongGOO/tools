#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright by zhaosonggo in 2024, All Rights Reserved.

import argparse
from core.plugin import Plugin


class ArgsParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Tools framework")
        self.subparsers = self.parser.add_subparsers(
            dest="plugin", help="Available plugins"
        )

    def init_subparsers(self, plugins: dict[str, Plugin]):
        for name in plugins:
            subparser = self.subparsers.add_parser(name, help=plugins[name].help())
            plugins[name].build_command_args(subparser)

    def parse_args(self):
        return self.parser.parse_args()

    def print_help(self):
        self.parser.print_help()
