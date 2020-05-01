# -*- coding: utf-8 -*-

import os

def right_directory():
    if os.getcwd().endswith("gitcourse"):
        return True
    else:
        return False


def is_repository():
    if ".git" in os.listdir(os.getcwd()):
        return True
    else:
        return False


def file_exists(file):
    if file in os.listdir(os.getcwd()):
        return True
    else:
        return False