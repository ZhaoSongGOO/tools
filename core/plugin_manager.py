#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright by zhaosonggo in 2024, All Rights Reserved.

from core.plugin import Plugin


class PluginManager:
    def __init__(self):
        self.plugins: dict[str, Plugin] = {}

    def register_plugin(self, plugin: Plugin):
        self.plugins[plugin.name] = plugin

    def dispatch_args(self, args):
        plugin = self.plugins[args.plugin]
        plugin.accept(args)
