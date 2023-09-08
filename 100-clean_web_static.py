#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives, using the function do_clean
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
        local("ls -1t | tail -n +{} | xargs -I {{}} "
              "rm -f {{}}".format(num + 1))
    with cd("/data/web_static/releases"):
        run("ls -1t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(num + 1))


if __name__ == "__main__":
    do_clean()
