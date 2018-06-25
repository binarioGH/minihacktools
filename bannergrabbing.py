#!/usr/bin/python
#-*-coding: utf-8-*-
import socket, sys

def h():
	print("\n\n-i: Agreagar una ip a la lista de host a escanear.")
	print("-if: Seleccionar un archivo con una lista de hosts a escanear.")
	print("-p: Agregar un puerto a la lista.")
	print("-pf: Seleccionar un archivo con puertos.")
	print("-vb: Seleccionar un archivo con los banners vulnerables.\n\n")
	exit()

def openfile(lst, f):
	try:
		file = open(f, "r")
	except:
		print("Problemas al abrir el siguiente archivo:\n{}".format(f))
	else:
		for line in f:
			lst.append(line)
		file.close()

def scann(ips, ports, vulbaners):
	#print("{}\n{}\n{}".format(ips,ports,vulbaners))
	#exit()
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(3)
	for ip in ips:
		for port in ports:
			try:
				ip = str(ip)
				port = int(port)
			except:
				continue
			else:
				try:
					sock.connect((ip, port))
					
				except:
					print("Problemas al conectarse a {} por el puerto {}".format(ip, port))
				else:
					print("Conectandose a {} por el puerto {}".format(ip, port))
					banner = str(sock.recv(1024))
					for vulbanner in vulbaners:
						if banner.strip() in vulbanner.strip():
							print("Se encontró un banner vulnerable: {}".format(banner))
							print("Host: {}".format(ip))
							print("Puerto: {}".format(port))
					sock.close()
 
if __name__ == '__main__':
	if len(sys.argv) < 7 and len(sys.argv) != 2:
			print("Por favor use {} -h para ver las opciones.".format(sys.argv[0]))
	else:
		ips = []
		ports = []
		vulbaners = []
		argcount = -1
		for arg in sys.argv:
			argcount += 1
			if arg[0] != "-":
				continue	
			elif arg == "-i":
				ips.append(sys.argv[argcount + 1])
			elif arg == "-if":
				openfile(ips, sys.argv[argcount + 1])
			elif arg == "-p":
				ports.append(sys.argv[argcount + 1])
			elif arg == "-pf":
				openfile(ports, sys.argv[argcount + 1])
			elif arg == "-vb":
				openfile(vulbaners, sys.argv[argcount + 1])
			elif arg == "-h":
				h()
			else:
			    print("'{}' No se reconoce como una bandera valida para este programa.".format(arg))
			scann(ips, ports, vulbaners)