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

    versions_dir = Path("versions")
    archives = sorted(versions_dir.glob("*"))
    for archive in archives[:-num]:
        archive.unlink()

    releases_dir = Path("/data/web_static/releases")
    archives = sorted(releases_dir.glob("web_static_*"), key=os.path.getctime)
    for archive in archives[:-num]:
        if archive.is_dir():
            shutil.rmtree(archive)
        else:
            archive.unlink()


if __name__ == "__main__":
    do_clean()
