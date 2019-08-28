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
	op.add_option("-n", "--doNotPrint",action="store_true", dest="doNotPrint", default=False, help="Use this flag if you don't want to print the output.")
	(o, args) = op.parse_args()
	if not o.dns:
		if not o.doNotPrint:
			print("You didn't defined a dns.")
		exit()
	if o.dns[:4].lower() == "www.":
		o.dns = o.dns[5:]
	commands = ("MX", "A", "AAAA", "NS", "TXT")
	answares = {}
	if o.saveLog:
		log = open(o.fileName, "w")
	for cmd in commands:
		try:
			answares[cmd] = resolver.query(o.dns, cmd)
		except:
			text = "DNS response do not contain {}.".format(cmd)
		else:
			text = "{} query solved!".format(cmd)
		finally:
			if o.saveLog:
				log.write(text+"\n")
			if not o.doNotPrint:
				print(text)
	if not o.doNotPrint:
		print("\n"+ "+"*80 + "\n")
	
	for ans in answares:
		
		responsetext = "  DNS RESPONSE FOR {}:".format(ans)
		if not o.doNotPrint:
			print("\n"+ "-"*80 + "\n")
			print(responsetext)
		if o.saveLog:
			log.write("\n"+ "-"*80 + "\n")
			log.write(responsetext+"\n")
		for info in answares[ans]:
			infoText = "\n	{}\n".format(info)
			if not o.doNotPrint:
				print(infoText)
			if o.saveLog:
				log.write("\n	{}\n".format(info)+"\n")

	if o.saveLog:
		log.close()

if __name__ == '__main__':
	main()