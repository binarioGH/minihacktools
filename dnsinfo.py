#-*-coding: utf-8-*-
from dns import resolver
from sys import argv

def main():
	dnsName = argv[1]
	commands = ("MX", "A", "AAAA", "NS", "TXT")
	answares = {}
	for cmd in commands:
		try:
			answares[cmd] = resolver.query(dnsName, cmd)
		except:
			print("DNS response do not contain {}.".format(cmd))
		else:
			print("{} query solved!".format(cmd))
	print("\n"+ "+"*80 + "\n")
	for ans in answares:
		print("\n"+ "-"*80 + "\n")
		print("DNS RESPONSE FOR {}:".format(ans))
		for info in answares[ans]:
			print("\n	{}\n".format(info))

if __name__ == '__main__':
	main()