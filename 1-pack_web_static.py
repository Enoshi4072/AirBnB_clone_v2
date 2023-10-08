#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Creates a compressed archive of the web_static folder."""
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_name))
        return archive_name
    except:
        return None

if __name__ == "__main__":
    result = do_pack()
    if result:
        print("web_static packed: {}".format(result))
    else:
        print("Packaging web_static failed.")

