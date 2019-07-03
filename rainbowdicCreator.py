#-*-coding: utf-8-*-
from hashlib import md5
from optparse import OptionParser as opt
from json import dumps
from time import strftime as date
from sys import argv
import codecs

getDate = lambda: "{}-{}".format(date("%d-%m-%y"), date("%H-%M-%S"))

def loadList(file):
	try:
		with codecs.open(file,"r",encoding="utf-8") as f:
			wlist = f.read().split()
	except Exception as e:
		print(e)
		return -1
	else:
		return wlist

def main():
	op = opt("Usage: %prog [flags] [values]")
	op.add_option("-i", "--inputFile", dest="inp",help="Set input file.")
	op.add_option("-o", "--outputFile", dest="out", help="Set the name of the output file.", default="{}.json".format(getDate()))
	(o, argv) = op.parse_args()
	words = loadList(o.inp)
	if words == -1:
		exit()
	jcontent = {"hashes":{}} #jcontent = json content
	for word in words:
		hash = md5(word.encode()).hexdigest()
		jcontent["hashes"][hash] = word
	try:
		with codecs.open(o.out, "w", encoding="utf-8") as jfile:
			jfile.write(dumps(jcontent, indent=4))
	except Exception as e:
		print(e)
		exit()
	else:
		print("Done!")


if __name__ == '__main__':
	main()
