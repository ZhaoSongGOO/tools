#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright by zhaosonggo in 2024, All Rights Reserved.


class Plugin:
    def __init__(self, name):
        self.name = name

    def help(self):
        pass

    def accept(self, args):
        pass

    def build_command_args(self, subparser):
        pass
