#-*-coding: utf-8-*-
from socket import *
from sys import argv
from optparse import OptionParser as opt

def connect(ip, port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(3)
	try:
		sock.connect((ip, port))
	except:
		return 0
	else:
		print("[+]Port {} is open.".format(port))
		try:
			banner = sock.recv(1024).decode().strip()
		except:
			pass
		else:
			print("[!]Banner: {}".format(banner))


def main():
	op = opt("Usage: %prog [flags] [values]")
	op.add_option("-t", "--target", dest="ip", default="uff", help="Set the target.")
	op.add_option("-p", '--ports', dest="ports", default="", help="Add specific ports: --ports 21,24,80")
	op.add_option("-n", "--min", dest="min", default=1, help="Set the minimum port for the range.")
	op.add_option("-x", "--max", dest="max", default=24, help="Set the maximum port for the range.")
	op.add_option("-r", "--norange", action="store_true", default=False, dest="norange", help="Do not use the range.")
	(o, argv) = op.parse_args()
	if o.ip == "uff":
		print("Set an Ip...")
		return -1

	try:
		o.min = int(o.min)
		o.max = int(o.max) + 1 
	except:
		print("Wrong range.")
		return -1
	o.ports = o.ports.split(",")
	portlist =[]
	for port in o.ports:
		try:
			portlist.append(int(port))
		except:
			print("[-]{} is not a port.".format(port))
			pass
	if o.norange:
		o.min = 0
		o.max = 0
	portlist += list(range(o.min, o.max))

	for port in portlist:
		connect(o.ip, port)


if __name__ == '__main__':
	main()