#-*-coding:utf-8-*-
from os import system
from sys import argv

def pingls():
	for ip in file:
		ping = system("ping {} > nul".format(ip))
		if ping == 0:
			print("{} está encendida.".format(ip))
		else:
			print("{} está apagada.".format(ip))
	exit()
def h():
	print("Programa para mandar ping a determinado numero de computadoras.\n")
	print("-ls: Se usa para dar una lista de ip a las que se les mandará ping.")
	print("-min: Se usa para determinar desde que numero de ip se empezará a mandar pings.")
	print("-max: Para determinar la ultima ip a la que se le mandará ping.")
	print("-s: Al usarla debes de determinar cual es tu subred.")
	print("Ejemplos:\n{} -s 192.168.0 -min 2 -max 10".format(argv[0]))
	print("{} -ls lista.txt".format(argv[0]))
	exit()
if __name__ == '__main__':
	if len(argv) != 7 and len(argv) != 2 and len(argv) != 3:
		print("Es probable que haya un error en la sintaxis, favor de revizar {} -h".format(argv[0]))
		exit()
	elif len(argv) == 3 and argv[1] == "-ls":	
		try:
			file = open(argv[2], "r")
		except:
			print("No se ha podido abrir:\n{}".format(argv[2]))
		else:
			pingls()
	elif len(argv) == 2 and argv[1] == "-h":
		h()
	else:
		subr = ""
		minim = int()
		maxim = int()
		argcount = -1
		for arg in argv:
			argcount += 1
			if arg[0] != "-":
				continue
			else:
				if arg == "-min":
					minim = argv[argcount + 1]
				elif arg == "-max":
					maxim = argv[argcount + 1]
				elif arg == "-s":
					subr = argv[argcount + 1]
				else:
					print("{} no se reconoce como una bandera valida.".format(arg))
					exit()
		for num in range(int(minim), int(maxim + 1)):
			ip = str("{}.{}".format(subr, num))
			ping = system("ping {} > nul".format(ip))
			if ping == 0:
				print("{} está encendida.".format(ip))
			else:
				print("{} está apagada.".format(ip))