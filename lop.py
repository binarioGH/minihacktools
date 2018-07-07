
#-*-coding: utf-8-*-
from os import system
from sys import argv
#Esta herramienta sigue en desarrollándose
#loppy significa lot of pings y el py significa python :) 
def h():
	name = argv[0]
	print("Este programa sirve para mandar pings a cierta cantidad de IPs.")
	print("Puede servir para descubrir que computadoras están encendidas en tu red.")
	print("Opciones:\n\n-n1: sierve para determinar el primer numero de la ip:\n{} -n1 192".format(name))
	print("Lo mismo pasa con -n2, 3 y 4.\nEjemplo: {} -n1 192 -n2 168 -n3 0 -n4 5".format(name))
	print("Tambien puedes hacer lo siguiete:\n{} -n1 192 -n2 168 -n3 0 -n4 1/10".format(name))
	print("de este modo se escaneará de la ip 192.168.0.1 a 192.168.0.10, esto se puede hacer con el resto.")
	print("-lst: Escoger un archivo donde hay varias ip a las cuales mandar ping.\nEjemplo:")
	print("{} -lst archivo_con_IPs.txt".format(name))
	print("Ejemplo: {} -n1 192 -n2 168 -n3 1/5 -n4 1/10".format(name))
	print("\n\nNotas:\nRevisa tu mascara de red antes de ejecutar este programa.")
	print("\nNo se puede usar -lst y -n1-5")
	exit()

def defminmax(n, minmax):
	minmax = str(minmax)
	num1 = ""
	num2 = ""
	count = 0
	slize = False
	for num in minmax:
		if num != "/":
			num1 = str(str(num1) + str(num))
			count += 1
			slize = True
		else: 
			try:
				num1 = int(num1)
			except Exception as e:
				print("\n\nHubo un problema al ejecutar el programa, revisa que todo esté correcto.")
				print("El problema quizá tenga que ver con: {}\n\n{}".format(n,e))
				print("\n\n{} {}".format(num1, num2))
				exit()
			else:
				try:
					num2 = int(minmax[count + 1:])
				except:
					pass
				nums[n][0] = num1
				nums[n][1] = num2
	if slize == True:
		try:
			try:
				num1 = int(num1)
			except:
				print(">:(")
			nums[n][0] = num1
			nums[n][1] = num1 + 1
		except Exception as e:
			print("\n\nHubo un problema al ejecutar el programa, revisa que todo esté bien.")
			print("El problema quizá tenga que ver con: {}\n\n{}".format(n,e))
			print("\n\n{} {}".format(num1, num2))
			exit()



def pingf(f):
	try:
		file = opne(f, "r")
	except:
		print("No se ha podido abrir el siguiente archivo:\n{}.".format(f))
	else:
		for line in file:
			ping = system("ping {}".format(line))	
			if ping == 0:
			    print("{} está vivo.".format(line))
			else:
			    print("{} no responde.".format(line))	
	exit()



if __name__ == '__main__':
	if len(argv) != 9 and len(argv) != 2 and len(argv) != 3:
		print("Usa {} -h para ver las opciones.".format(argv[0]))
		exit()
	else:
		segment = str()
		nums = {"n1":[0,0],"n2":[0,0],"n3":[0,0],"n4":[0,0]}
		argcount = -1
		for arg in argv:
			argcount += 1
			if arg[0] != "-":
				continue
			elif arg == "-h":
				h()
			elif arg == "-n1":
				defminmax("n1", str(argv[argcount + 1]))
			elif arg == "-n2":
				defminmax("n2", str(argv[argcount + 1]))
			elif arg == "-n3":
				defminmax("n3", str(argv[argcount + 1]))
			elif arg == "-n4":
				breakpoint()
				defminmax("n4", str(argv[argcount + 1]))
			elif arg == "-lst":
				pingf(argv[argcount + 1])
			else:
				print("Usa {} -h para ver las opciones.".format(argv[0]))
				exit()
			print(nums)
		for n1 in range(nums["n1"][0], nums["n1"][1]):
			for n2 in range(nums["n2"][0], nums["n1"][1]):
				for n3 in range(nums["n3"][0], nums["n3"][1]):
					for n4 in range(nums["n4"][0], nums["n4"][1]):
						ip = "{}.{}.{}.{}".format(n1,n2,n3,n4)
						ping = system("ping {}".format(ip))
						if ping == 0:
							print("{} está vivo.".format(ip))
						else:
							print("{} no responde.".format(ip))