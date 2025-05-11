#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright by zhaosonggo in 2024, All Rights Reserved.
import datetime
import sys


def get_format_time_str():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d %H:%M:%S")
    return formatted_time


class BaseLog:
    def info(self, msg):
        pass

    def success(self, msg):
        pass

    def error(self, msg):
        pass

    def fatal(self, msg):
        pass

    def warning(self, msg):
        pass


class Log:
    green_color_code = "\033[92m"
    red_color_code = "\033[91m"
    yellow_color_code = "\033[93m"
    blue_color_code = "\033[94m"
    reset_color_code = "\033[0m"

    @staticmethod
    def print(msg):
        print(msg, flush=True)

    @staticmethod
    def info(msg):
        print_msg = f"[TOOLS][INFO] {msg}"
        print(
            f"{Log.blue_color_code}[{get_format_time_str()}]{print_msg}{Log.reset_color_code}",
            flush=True,
        )

    @staticmethod
    def success(msg):
        print_msg = f"[TOOLS][SUCCESS] {msg}"
        print(
            f"{Log.green_color_code}[{get_format_time_str()}]{print_msg}{Log.reset_color_code}",
            flush=True,
        )

    @staticmethod
    def error(msg):
        print_msg = f"[TOOLS][ERROR] {msg}"
        print(
            f"{Log.red_color_code}[{get_format_time_str()}]{print_msg}{Log.reset_color_code}",
            flush=True,
        )

    @staticmethod
    def fatal(msg):
        print_msg = f"[TOOLS][FATAL] {msg}"
        print(
            f"{Log.red_color_code}[{get_format_time_str()}]{print_msg}{Log.reset_color_code}",
            flush=True,
        )
        sys.exit(1)

    @staticmethod
    def warning(msg):
        print_msg = f"[TOOLS][WARNING] {msg}"
        print(
            f"{Log.yellow_color_code}[{get_format_time_str()}]{print_msg}{Log.reset_color_code}",
            flush=True,
        )
