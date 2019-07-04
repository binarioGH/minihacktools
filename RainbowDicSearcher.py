#-*-coding: utf-8-*-
from json import loads
from sys import argv
from optparse import OptionParser as opt
from time import strftime
import codecs

getDate = lambda: "{}-{}".format(strftime("%d-%m-%y"), strftime("%H-%M-%S"))

def loadFile(file, splt=False):
	try:
		with codecs.open(file, "r", encoding="utf-8") as f:
			content = f.read()
	except Exception as e:
		print(e)
		return -1
	else:
		if splt:
			content = content.split()
		return content

def searchHash(*hashes, rd, prnt=True):
	raindic = loadFile(rd)
	if raindic == -1:
		return ("There was a problem loading {}.".format(rd), [0])
	raindic = loads(raindic)
	hacked = []
	for hsh in hashes:
		print(hsh)
		exit()
		if hsh in raindic["hashes"]:
			if prnt:
				print("{} : {}".format(hsh, raindic["hashes"][hsh]))
			hacked.append("{}:{}".format(hsh,raindic["hashes"][hsh]))
	return ("{} hashes found".format(len(hacked)), hacked)




def main():
	op = opt("Usage: %prog [flags] [values]")
	op.add_option("-j", "--json", dest="json", help="Set json file.", default="undefined")
	op.add_option("-H", "--hash", dest="hash", help="Define the hash to brake.", default="undefined")
	op.add_option("-p", "--dontprint", dest="prnt", help="Do not show output.", action="store_false", default=True)
	op.add_option("-s", "--save", dest="save", help="Use this flag to save your results.", action="store_true", default=False)
	op.add_option("-l", "--logname", dest="log", help="Set log name.", default=getDate())
	op.add_option("-f", "--inputfile", dest="hashes",help="Set a file with hashes to search.", default="undefined")
	(o, argv) = op.parse_args()
	if o.json == "undefined" or (o.hash == "undefined" and o.hashes == "undefined"):
		print("Values undefined:\nJson file: {}\nHash: {}".format(o.json, o.hash))
		exit()
	if o.hashes == "undefined":
		hashes = []
	else:
		hashes = loadFile(o.hashes, True)
	if o.hash != "undefined":
		hashes.append(o.hash)
	out, lst = searchHash(hashes, rd=o.json, prnt=o.prnt)
	if o.prnt:
		print(out)
	if o.save:
		try:
			with open(o.log, "w") as log:
				log.write("\n".join(lst))
		except Exception as e:
			if o.prnt:
				print(e)
	if o.prnt:
		print("Done!")

	
if __name__ == '__main__':
	main()