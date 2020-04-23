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


def maintxt_exists():
    if "main.txt" in os.listdir(os.getcwd()):
        return True
    else:
        return False


def mainlog_exists():
    if "main.log" in os.listdir(os.getcwd()):
        return True
    else:
        return False