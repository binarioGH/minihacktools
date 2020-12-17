#!/usr/bin/py
from os import listdir


contnet = listdir('/run/user/1000/gvfs')
counter = 0
for file in content:
	if "smb" in file:
		print("--	/run/user/1000/gvfs/{}\n\n".format(file))
		counter += 1

print("Total SMB dirs: {}".format(counter))