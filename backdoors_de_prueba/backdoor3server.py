#!/usr/bin/python
#-*-coding:utf-8-*-
from socket import *
from os import system, getcwd

if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(("127.0.0.1",5000))
	sock.listen(1)
	conn, addr = sock.accept()
	while True:
		msg = conn.recv(1024).decode()
		try:
			system(msg)
		except:
			conn.send("No se ha podido ejecutar el comando.\n{}".format(getcwd()).encode())
		else:
			conn.send("Se ha ejecutado el comando.\n{}".format(getcwd()).encode())
