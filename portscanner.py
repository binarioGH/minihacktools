#!/usr/bin/python
#-*-coding: utf-8 -*-
from socket import *
from sys import argv
def banner():
	print('''           
        
                 ___________                
		|           |                    
		|    ___    |        
		|   |___|   |  S    
		|     ______|     
		|    |         
		|    |         
		|    |         
		|____|        
		''')
def bannerscann(banners, bf):
	try:
		vulbanners = open(bf, "r")
	except:
		print("No se ha podido abrir {}".format(b))
		exit()
	else:
		print("Se ha empezado el analisis de banners.\n\n")
		for banner in banners:
			banner += "\n"
			print("[+] Analizando: {}".format(banner))
			count = 0
			for b in vulbanners:
				count += 1
				if b in banner or b == banner:
					print("Se ha encontrado un banner vulnerable: {}".format(b))
					break
		print("Se ha terminado el analisis de banners.")


def portscann(minim, maxim):
	bnners = []
	print("\nSe ha empezado el analisis de puertos...\n")
	
	for port in range(minim, maxim + 1):
		server = socket(AF_INET, SOCK_STREAM)
		server.settimeout(2)
		if(server.connect_ex((ip, port)) == 0):
			print("\n\nPuerto abierto: {}.".format(port))
			try:
				banner = server.recv(1024).decode()
				print("Banner: {}".format(banner))
				bnners.append(banner)
			except:
				continue
			server.close()
	print("\n\nAnalisis de puertos terminado.")
	return bnners

def h():
	print("Usos: {}: [-min num] [-max num] [-i ip] [-vb archivo]\n\n".format(argv[0]))
	print("Opciones:\n\n-min: Establecer el puerto por el que se empezará a escanear.")
	print("-max: Establecer el ultimo puerto que se escaneará.")
	print("-i: Establecer que la ip del host que se va a escanear.")
	print("-vb: Analizar los banners vulnerables (Tienes que agregar un archivo con banners vulnerables).")
	exit()

if __name__ == '__main__':
	banner()
	if len(argv) != 7 and len(argv) != 2 and len(argv) != 9:
		print("Usa {} -h para ver las opciones.".format(argv[0]))
		exit()
	else:
		ip = str()
		minim = 0
		maxim = 0
		argcount = 0
		vb = ""
		vbe = False
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
			elif arg == "-vb":
				vb = argv[argcount + 1]
				vbe = True
			else:
				print("Usa {} -h para ver las opciones.".format(argv[0]))
				exit()
			argcount += 1

		print("{} {} {}".format(minim, maxim, ip))
		bnners = portscann(minim, maxim)
		if vbe == True:
			bannerscann(bnners, vb)
		else:
			exit()

		