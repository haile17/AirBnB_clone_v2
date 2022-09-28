#!/usr/bin/python3
# fbric script that generates a tgz archive from the content web_static
# folder of the AirBnB clone repo

from datatime import datatime
from fabric.api import local
from os.path import isdir

def do_pack():
	"""generates a tgz archive"""
	try:
		data = datatime.now().strftime("Y%m%d%H%M%S")
		if isdir("versions") is False:
			local ("mkdir version")
		file_name = "version/web_static_{}.tgz".format(data)
		local("tar -cvzf {} web_static".format(file_name))
		return file_name
	except:
		return None 
