#!/usr/bin/python3
"""
Script that distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ["18.204.14.252", "107.22.144.202"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Distributes an archive to teh web servers.
    """
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        folder_name = archive_path.split("/")[-1].split(".")[0]
        release_path = "/data/web_static/releases/{}".format(folder_name)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{}.tgz -C {}".format(folder_name, release_path))
        run("rm /tmp/{}.tgz".format(folder_name))
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        print("New version deployed!")
        return True
    except Exception as error:
        return False
