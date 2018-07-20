#-*-coding: utf-8 -*-
#El programa está inspirado en los siguientes links:
#http://www.pythondiario.com/2018/05/proyecto-facescraped-extractor-de.html
#https://github.com/LuisAlejandroSalcedo/FaceScraped
from sys import argv
from datetime import datetime
import os
try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen
from random import randint

class Scrapper():
	def __init__(self):
		if len(argv) != 2:
			print("Solo utilice:\n{} (algún numero)".format(argv[0]))
		else:
			try:
				argv[1] = int(argv[1])
			except:
				print("Argumento incorrecto, tienes que poner un numero.")
				exit()
	def main(self, num):
		pid = randint(1, int(1e7))
		pcount = 0
		dcount = 0
		try:
			folder = "FaceScrapped{}".format(randint(100,1000))
			os.mkdir(str(folder))
		except Exception as e:
			print("Ha habido un problema al crear un directorio.\n{}".format(e))
			exit()
		print("Se ha creado el directorio {}".format(folder))
		while pcount < num:
			photourl = "http://graph.facebook.com/picture?id={}&width=800".format(pid)
			if self.getprofile(photourl,"{}/{}.jpg".format(folder,pid)):
			    print("Se ha descargado {}.".format(photourl))
			    pcount += 1
			    pid += 1
			else:
				dcount += 1
				if dcount != 20:
					pid += 10
				else:
					dcount = 0
					print("No se han encontrado imagenes en las anteriores id ({})...".format(pid))
					pid = randint(1, int(1e7))
					print("...Se ha conseguido un nuevo numero de id: {}".format(pid))

	def getprofile(self, photourl, saveurl):
		response = urlopen(photourl)
		if response.geturl() != "https://static.xx.fbcdn.net/rsrc.php/v3/yo/r/UlIqmHJn-SK.gif":
			open(saveurl, "wb").write(response.read())
			return True
		return False

		

if __name__ == '__main__':
	start = Scrapper()
	start.main(argv[1])
