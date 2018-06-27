#-*-coding: utf-8-*-
import socket
if __name__ == '__main__':
	host = "192.168.0.8"
	port = 5000
	server = socket.socket()
	server.bind((host,port))
	server.listen(1)
	conn, addr = server.accept()
	print("Conexión establecida: {}".format(addr))
	while True:
		mensaje = conn.recv(1024).decode()
		print("El cliente ha enviado: {}".format(mensaje))
		resp = input("Responder: ")
		if resp == "exit":
			server.close()
			exit()
		else:
			conn.send(resp.encode())

