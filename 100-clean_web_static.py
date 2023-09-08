#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives, using the function do_clean.
"""
from fabric.api import *
import os

env.hosts = ["18.204.14.252", "107.22.144.202"]


def do_clean(num=0):
    """
    Deletes out-of-date archives.
    """
    if num:
        num = int(num)
    else:
        num = 1

    with lcd("versions"):
        archives = sorted(os.listdir("."))
        [archives.pop() for i in range(num)]
        [local("rm -f ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr | grep 'web_static_'").split()
        [archives.pop() for i in range(num)]
        [run("rm -rf ./{}".format(a)) for a in archives]


if __name__ == "__main__":
    do_clean()
