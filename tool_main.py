#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright by zhaosonggo in 2024, All Rights Reserved.

from core.plugin_manager import PluginManager
from core.args_parser import ArgsParser
from plugins.code_format.code_format_plugin import CodeFormatPlugin
from plugins.clang_tidy.clang_tidy_plugin import ClangTidyPlugin


def main():
    plugin_manager = PluginManager()
    plugin_manager.register_plugin(CodeFormatPlugin())
    plugin_manager.register_plugin(ClangTidyPlugin())
    args_parser = ArgsParser()
    args_parser.init_subparsers(plugin_manager.plugins)
    args = args_parser.parse_args()

    if args.plugin is not None:
        plugin_manager.dispatch_args(args)
    else:
        args_parser.print_help()


if __name__ == "__main__":
    main()
