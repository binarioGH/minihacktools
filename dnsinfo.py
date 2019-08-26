#-*-coding: utf-8-*-
from dns import resolver
from sys import argv
from optparse import OptionParser as opt
from time import strftime as d
getDate = lambda: d("%m-%d-%y-%H-%M-%S")
def main():
	op = opt("Usage: %prog [flgas] [values]")
	op.add_option("-d", "--dns", dest="dns", default=0, help="Set the dns that you are investigating.")
	op.add_option("-s", "--save",action="store_true" ,dest="saveLog", default=False, help="Save all the information in a file.")
	op.add_option("-f", "--filename", dest="fileName",default="{}.txt".format(getDate()), help="Set a the name of the file where the log is gonna be saved.")
	(o, args) = op.parse_args()
	commands = ("MX", "A", "AAAA", "NS", "TXT")
	answares = {}
	if o.saveLog:
		log = open(o.fileName, "w")
	for cmd in commands:
		try:
			answares[cmd] = resolver.query(o.dns, cmd)
		except:
			text = "DNS response do not contain {}.".format(cmd)
			print(text)
		else:
			text = "{} query solved!".format(cmd)
			print(text)
		finally:
			if o.saveLog:
				log.write(text+"\n")
	print("\n"+ "+"*80 + "\n")
	
	for ans in answares:
		print("\n"+ "-"*80 + "\n")
		responsetext = "  DNS RESPONSE FOR {}:".format(ans)
		print(responsetext)
		if o.saveLog:
			log.write("\n"+ "-"*80 + "\n")
			log.write(responsetext+"\n")
		for info in answares[ans]:
			infoText = "\n	{}\n".format(info)
			print(infoText)
			if o.saveLog:
				log.write("\n	{}\n".format(info)+"\n")

	if o.saveLog:
		log.close()

if __name__ == '__main__':
	main()