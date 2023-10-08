#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import env, put, run
from os.path import exists
env.hosts = ['100.26.166.61', '52.91.117.189']


def do_deploy(archive_path):
    """Deploys archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split("/")[-1]
        archive_no_ext = archive_filename.split(".")[0]

        # Upload archive to /tmp/
        put(archive_path, "/tmp/")

        # Create the release directory
        run("mkdir -p /data/web_static/releases/{}/".format(archive_no_ext))

        # Uncompress archive into release directory
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_filename, archive_no_ext))

        # Delete the archive from /tmp/
        run("rm /tmp/{}".format(archive_filename))

        # Move contents to the web_static folder
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"
            .format(archive_no_ext, archive_no_ext))

        # Remove the empty web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_no_ext))

        # Delete the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_no_ext))

        print("New version deployed!")
        return True

    except Exception as e:
        return False
