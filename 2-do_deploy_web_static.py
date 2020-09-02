#!/usr/bin/python3
"""Module"""


def do_deploy(archive_path):
    """Fabric scriptthat distributes anarchive to your web servers"""
    time_file = time.strftime('%Y%m%d%H%M%S')
    try:
        local("mkdir -p versions")
        local("tar -zxv1f versions/web_static_{:s}.tgz web_static/".format
              (time_file))
        return ("versions/web_static_{}.tgz".format(time_file))
    except path:
        return None
