#!/usr/bin/python3
#-*-coding: utf-8-*-
from socket import *

if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	ip = input("Ingresa la ip de el objetivo: ")
	port = int(input("Ingresa el puerto: "))
	try:
		sock.connect((ip,port))
	except:
		print("No se ha podido conectar a {} por el puerto {}".format(ip, port))
		exit()
	else:
		print("Se ha conectado con exito a {} por el puerto {}".format(ip, port))
		while True:
			sock.send(input(">>").encode())
			print(sock.recv(1024).decode())
 