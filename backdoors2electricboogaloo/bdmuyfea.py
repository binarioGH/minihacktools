#-*-coding: utf-8-*-
from socket import *
if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(("0.0.0.0", 5000))
	sock.listen(1)
	conn, addr = sock.accept()
	while True:
		cmd = conn.recv(1024).decode()
		try:
			exec(cmd)
		except Exception as e:
			conn.send("{}".format(e).encode())

