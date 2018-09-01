#-*-coding: utf-8-*-
from socket import *
import threading
from os import system, getcwd
from getpass import getpass
from time import sleep



class Botmaster:
	def __init__(self, c):
		self.clean = c
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
				system(self.clean)
				cmd = ""
				recvstrings = threading.Thread(target=self.waiting4recv)
				recvstrings.daemon = True
				recvstrings.start()
				print("Input 'exit' to go back.")
				while cmd != "exit":
					cmd = input(">>>>")
					if cmd != "exit":
						self.sock.send(cmd.encode())
				self.sock.close()
				sleep(2)
				getpass("Press 'enter' to continue...")
	def waiting4recv(self):
		print("Starting 'waiting4recv' method...")
		while True:
			try:
				r = self.sock.recv(1024).decode()
				try:
					print("{}\n>>>>".format(r))
				except:
					pass
			except:
				print("Closing 'waiting4recv' method.")
				return 0



if __name__ == '__main__':
	d = getcwd()
	if d[0].isalpha:
		clean = "cls"
	else:
		clean = "clear"

	bm = Botmaster(clean)
	do = ""
	IPs = []
	ports = []
	while do != "exit":
		system(clean)
		do = input('''
		  - B O T   M A S T E R -
			___________________
			[C]onnect to a bot
			[S]how register of connections
			[exit]
			>>>>''')
		do = do.lower()
		if do == "c":
			botip = input("Input the IP of the new bot: ")
			IPs.append(botip)
			botport = input("Input the port that you are going to use to connect to the bot: ")
			ports.append(botport)
			bm.conn2bot(botip, botport)
			try:
				bm.sock.close()
			except:
				pass
		elif do == "s":
			count = 0
			system("cls")
			for i in IPs:
				print("-------------------")
				print("ip: {}\nport: {}".format(IPs[count], ports[count]))
				print("-------------------")
				count += 1
			getpass("Press 'enter' to continue...")