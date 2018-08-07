#!/urs/bin/python
#-*-coding: utf-8-*-
from socket import *
from sys import argv

def h():
	print("\nDebes usar esta sintaxis:\n{} (objetivo) (comando) (archivo con usuarios)".format(argv[0]))
	exit()


if __name__ == '__main__':
	try:
		if argv[1] == "-h":
			h()
		target = argv[1]
		command = argv[2]
		file = argv[3]

	except:
		print("{} -h para ver las opciones".format(argv[0]))
		exit()

	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(5)
	try:
		sock.connect((target,25))
		banner = sock.recv(1024).decode()
		print(banner)
		if "220" in banner:
			with open(file, "r") as f:
				for user in f:
					sock.send("{} {}".format(command ,user).encode())
					result = sock.recv(1024).decode()
					if "252" in str(result) or "250" in str(result):
						print("Usuario valido: {}".format(user))
		sock.close()
	except Exception as e:
		print(e)




