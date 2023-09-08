#!/usr/bin/python3
"""
script that creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import *
from os.path import exists
from datetime import datetime
import os

env.hosts = ["18.204.14.252", "107.22.144.202"]


def do_pack():
    """
    Generates .tgz archive from contents of the web_static folder.
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    result = local("tar -czvf {} web_static".format(archive_name))
    if result.succeeded:
        return archive_name
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not exists(archive_path):
        return False
    filename = archive_path.split('/')[-1]
    folder_name = filename.split('.')[0]
    no_tgz = "/data/web_static/releases/" + folder_name
    tmp = "/tmp/" + filename
    try:
        put(archive_path, "/tmp/")
        release_path = "/data/web_static/releases/" + folder_name

        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(tmp, release_path))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        return True
    except Exception as error:
        return False


def deploy():
    """
    Creates and deploys the archive to the servers.
    """
    arc_path = do_pack()
    if not arc_path:
        return False
    return do_deploy(arc_path)
