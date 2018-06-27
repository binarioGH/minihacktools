#!/usr/bin/python
#-*-coding: utf-8 -*-
from socket import *
from sys import argv

def h():
	print("Opciones:\n\n-min: Establecer el puerto por el que se empezará a escanear.")
	print("-max: Establecer el ultimo puerto que se escaneará.")
	print("-i: Establecer que la ip del host que se va a escanear.")
	exit()

if __name__ == '__main__':
	if len(argv) != 7 and len(argv) != 2:
		print("Usa {} -h para ver las opciones.".format(argv[0]))
		exit()
	else:
		ip = str()
		minim = 0
		maxim = 0
		argcount = 0
		for arg in argv:
			if arg[0] != "-":
				argcount += 1
				continue
			elif arg == "-h":
				h()
			elif arg == "-i":
				ip = argv[argcount + 1]
			elif arg == "-min":
				minim = int(argv[argcount + 1])
			elif arg == "-max":
				maxim = int(argv[argcount + 1])
			else:
				print("Usa {} -h para ver las opciones.".format(argv[0]))
				exit()
			argcount += 1
		for port in range(minim, maxim + 1):
			server = socket(AF_INET, SOCK_STREAM)
			server.settimeout(2)
			if(server.connect_ex((ip, port)) == 0):
				print("\n\nPuerto abierto: {}.".format(port))
			try:
				print("Banner: {}".format(server.recv(1024)))
			except:
				continue
			server.close()