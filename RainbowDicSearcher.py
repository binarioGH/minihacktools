#-*-coding: utf-8-*-
from json import loads
from sys import argv
from optparse import OptionParser as opt
import codecs
def loadFile(file):
	try:
		with codecs.open(file, "r", encoding="utf-8") as f:
			content = f.read()
	except Exception as e:
		print(e)
		return -1
	else:
		return content

def main():
	op = opt("Usage: %prog [flags] [values]")
	op.add_option("-j", "--json", dest="json", help="Set json file.", default="undefined")
	op.add_option("-H", "--hash", dest="hash", help="Define the hash to brake.", default="undefined")
	(o, argv) = op.parse_args()
	if o.json == "undefined" or o.hash == "undefined":
		print("Values undefined:\nJson file: {}\nHash: {}".format(o.json, o.hash))
		exit()
	rainbowDic = loadFile(o.json)
	if rainbowDic == -1:
		exit()
	rainbowDic = loads(rainbowDic)
	if o.hash in rainbowDic["hashes"]:
		print("{} : {}".format(o.hash, rainbowDic["hashes"][o.hash]))
	else:
		print("{} was not found in the Rainbo Dictionary file.".format(o.hash))

if __name__ == '__main__':
	main()