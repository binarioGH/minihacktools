#-*-coding: utf-8-*-
from imaplib import IMAP4_SSL as imap
from email import message_from_string as emailinfo
from sys import argv
from subprocess import run, PIPE 
from time import strftime as date
from threading import Thread
from smtplib import SMTP
from email.mime.text import MIMEText
from os import chdir, getcwd

getDate = lambda: "{}-{}".format(date("%d %m %y"), date("%H:%M:%S"))

class Mailer:
	def __init__(self,user, passw, server="smtp.gmail.com:587"):
		self.user = user
		self.passw = passw
		self.mail = SMTP(server)
		self.mail.starttls()
		self.mail.login(self.user, self.passw)
	def send(self,msj, to, sbj=getDate()):
		mime = MIMEText(msj)
		mime["From"] = self.user
		mime["To"] = to
		mime["Subject" ] = sbj 
		mime = mime.as_string()	 
		self.mail.sendmail(self.user, to, mime)

def getOutput(cmd):
	resp = run(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	stdout = resp.stdout.decode("latin1")
	stderr = resp.stderr.decode("latin1")
	out = "{}{}".format(stdout,stderr)
	return out

def getFrom(f):
	f = f.split()
	f = f[-1][1:-1]
	return f

def getCommands(conn, smtp, selected="INBOX"):
	lastmsj = ""
	while True:
		try:
			conn.select(selected)
			result, data = conn.uid("search", None, "HEADER Subject 'cmd:'") 
		except Exception as e:	
			print(e)
			continue
		messajes = data[0].split()
		if len(messajes) == 0:
			continue
		if messajes[-1] == lastmsj:
			continue
		else:
			lastmsj = messajes[-1]
			print("\nNew message!")
		result, data = conn.uid("fetch", lastmsj, "(RFC822)")
		raw = data[0][1].decode("utf-8")
		mail = emailinfo(raw)
		command = mail["Subject"][4:]
		if command[:2].lower() == "cd":
			try:
				chdir(command[3:])
			except:
				pass
		out = getOutput(command)
		sendto = getFrom(mail["From"])
		smtp.send(out, sendto, "{} {}".format(command, getDate()))


def main():
	user = argv[1]
	passw = argv[2]
	smtp = Mailer(user, passw)
	conn = imap("imap.gmail.com")
	conn.login(user, passw)
	getmsj = Thread(target=getCommands, args=[conn, smtp,])
	getmsj.daemon = True
	getmsj.start()
	cmd = ""
	while cmd != "exit":
		cmd = input(">")
		if cmd == "cls":
			run("cls", shell=True)
	exit()
if __name__ == '__main__':
	main()