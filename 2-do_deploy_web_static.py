#!/usr/bin/python3
"""
Script that distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import *
from os.path import exists, join
from datetime import datetime

env.hosts = ["18.204.14.252", "107.22.144.202"]


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not exists(archive_path):
        return False

    filename = archive_path.split('/')[-1]
    folder_name = filename.split('.')[0]
    no_tgz = join("/data/web_static/releases", folder_name)
    tmp = join("/tmp", filename)

    try:
        put(archive_path, "/tmp/")
        release_path = join("/data/web_static/releases", folder_name)

        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(tmp, release_path))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        print("New version deployed!")
        return True
    except Exception as error:
        return False
