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
	op.add_option("-0","--dMX", dest="mx", action="store_false" ,default=True, help="Do not query MX records. (Mail Exchange)")
	op.add_option("-1", "--dA", dest="a", action="store_false", default=True, help="Do not query A records. (IPV4)")
	op.add_option("-2", "--dAAAA", dest="aaaa", action="store_false", default=True, help="Do not query AAAA records (IPV6)")
	op.add_option("-3", "--dNS", dest="ns", action="store_false", default=True, help="Do not query NS records (Name Service)")
	op.add_option("-4", "--dTXT", dest="txt", action="store_false", default=True, help="Do not query TXT records (Text records)")
	op.add_option("-o", "--otherrecord", dest="otherrecord", default=0, help="Set other records that you want to search. --otherrecord one,two,three...")	
	(o, args) = op.parse_args()
	if not o.dns:
		if not o.doNotPrint:
			print("You didn't defined a dns.")
		exit()

	if o.dns[:4].lower() == "www.":
		o.dns = o.dns[5:]
	commands = {"MX": [o.mx], "A": [o.a], "AAAA": [o.aaaa], "NS": [o.ns], "TXT": [o.txt]}
	if o.otherrecord:
		o.otherrecord = o.otherrecord.split(",")
		for record in o.otherrecord:
			record = record.upper()
			commands[record] = [True]
	if o.saveLog:
		log = open(o.fileName, "w")
	for cmd in commands:
		text =""
		try:
			if commands[cmd][0]:
				commands[cmd].append(resolver.query(o.dns, cmd))
			else:
				continue
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
	
	for cmd in commands:
		if not commands[cmd][0]:
			continue
		responsetext = "  DNS RESPONSE FOR {}:".format(cmd)
		if not o.doNotPrint:
			print("\n"+ "-"*80 + "\n")
			print(responsetext)
		if o.saveLog:
			log.write("\n"+ "-"*80 + "\n")
			log.write(responsetext+"\n")
		for info in commands[cmd][1]:
			infoText = "\n	{}\n".format(info)
			if not o.doNotPrint:
				print(infoText)
			if o.saveLog:
				log.write("\n	{}\n".format(info)+"\n")

	if o.saveLog:
		log.close()

if __name__ == '__main__':
	main()