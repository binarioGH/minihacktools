#-*-coding: utf-8-*-
from hashlib import md5
from sys import argv
def gethash(file):
	with open(file, "rb") as f:
		hsh = md5(f.read()).hexdigest()
		return hsh
if __name__ == '__main__':
	f = argv[1]
	print(gethash(f))