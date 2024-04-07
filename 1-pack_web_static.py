#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Path to the created .tgz archive if successful, otherwise None.
    """
    dt = datetime.now()
    local("mkdir -p versions")
    timestamp = dt.strftime("%Y%m%d%H%M%S")
    file = "web_static_{}.tgz".format(timestamp)
    # Compress the web_static folder into the .tgz archive
    result = local("tar -cvzf versions/{} web_static".format(file))

    # Check if the archive was created successfully
    if result.succeeded:
        return "versions/{}".format(file)
    else:
        return None
