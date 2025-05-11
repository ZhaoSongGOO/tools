#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright by zhaosonggo in 2024, All Rights Reserved.

import os


class ChangeList:
    def __init__(self):
        pass

    def is_ignored(self, item, ignored_list):
        for i in ignored_list:
            try:
                if os.path.samefile(item, i):
                    return True
            except:
                # if i is not exist, continue
                continue
        return False

    def get_changed_files(self):
        commit_change_info = os.popen("git diff HEAD^ --name-only").readlines()
        change_file_list = []
        index = len(commit_change_info) - 1
        while index >= 0:
            if commit_change_info[index] == "\n":
                break
            else:
                item = commit_change_info[index].split()[-1]
                change_file_list.append(item)
            index -= 1
        return change_file_list

    def get_all_files_from_root(self, path):
        files = []
        if os.path.isfile(path):
            files.append(path)
        elif os.path.isdir(path):
            file_list = os.listdir(path)
            check_file_list = file_list[:]
            if ".checkignore" in file_list:
                ignored_file = []
                ignore_file_path = os.path.join(path, ".checkignore")
                fd = open(ignore_file_path)
                for ignore_item in fd.readlines():
                    ignored_file.append(os.path.join(path, ignore_item).rstrip())
                ignored_file.append(ignore_file_path)
                check_file_list = [
                    item
                    for item in file_list
                    if not self.is_ignored(os.path.join(path, item), ignored_file)
                ]
            for f in check_file_list:
                files += self.get_all_files_from_root(os.path.join(path, f))
        return files
