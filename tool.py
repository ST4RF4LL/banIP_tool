#! /usr/bin/env python2
# coding: utf-8
import os
import re


def log_operation():
    pass


def get_lastb():
    result = os.popen("lastb -n 100")
    for line in result:
        # print line
        ip = re.findall(r'\d+.\d+.\d+.\d+', line)[0]
        print ip
        # TODO compare with log list


def cmd_creater():
    pass


if __name__ == "__main__":
    get_lastb()
