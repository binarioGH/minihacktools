#-*-coding: utf-8-*-
import subprocess
from whois import whois
from platform import python_version as pv
from platform import platform as so
from os import system 


		
if __name__ == '__main__':
	if str(so())[0] == "W": 
		clear = "cls"
	else: 
		clear = "clear"
	if str(pv()) == "3": 
 		raw_input = input

	cmd = ""
	starget = False
	prompt = "Select a target"
	data = []
	while cmd.lower() != "exit":
		try:
			cmd = input("({})-|>>>>".format(prompt))
			if starget == False:
				ping = subprocess.run("ping {}".format(cmd), stdout=subprocess.DEVNULL)
				if str(ping)[len(str(ping)) - 2] == "0":
					starget = True
					prompt = cmd
					who = whois(cmd)
					for d in who:
						data.append(d)

				else:
					print("The url does not respond.")
			else:
				if cmd == "end":
					prompt = "Select a target"
					starget = False
				elif cmd == "help":
					for d in data:
						print(d)
				elif cmd == clear:
					system(clear)
				else:
					if cmd in data:
						print(who[cmd])
					else:
						print("That data does not exist.")
		except Exception as e:
			print(e)



		


