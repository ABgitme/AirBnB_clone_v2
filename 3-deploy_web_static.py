#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
from os.path import exists
from datetime import datetime
from fabric.api import env
from fabric.api import local, put, run


env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
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


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if exists(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file, name))
        run("rm /tmp/{}".format(file))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name))
        return True
    except Exception as e:
        print(f"Error:{e}")
        return False


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
