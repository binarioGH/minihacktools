#-*-coding: utf-8-*-
from time import strftime
from subprocess import run
from random import randint
def startLink(link):
	run("start {}".format(link), shell=True)


def main():
	date = strftime("%d/%m/%y")
	print(date)
	if date == "23/08/19":
		print("El día de los miados ha llegado")
		links_miados = (
			"https://www.youtube.com/watch?v=KCWEedgFNCk",
			"https://www.youtube.com/watch?v=Ky22ke22IVA",
			"https://www.youtube.com/watch?v=oKK3xwRDAys",
			"https://www.youtube.com/watch?v=w8dqPJYIA2U",
			"https://www.youtube.com/watch?v=XR1GF-AgSPQ"
			)
		link_seleccionado = links_miados[randint(0, len(links_miados) - 1)]
		startLink(link_seleccionado)

if __name__ == '__main__':
	main()