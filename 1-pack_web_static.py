#!/usr/bin/python3
# fbric script that generates a tgz archive from the content web_static
# folder of the AirBnB clone repo

from datetime import datetime
from fabric.api import local
from fabric.decorators import runs_once

@runs_once
def do_pack():

	"""generates a tgz archive"""
	local("mkdir -p versions")
	path = ("version/web_static_{}.tgz"
					.format(datetime.strftime(datetime.now(), "Y%m%d%H%M%S")))
	result = local("tar -cvzf {} web_static".format(path))
	if result.failed:
		return None
	return path
