#-*-coding: utf-8-*-
from time import strftime
from subprocess import run

def startLink(link):
	run("start {}".format(link), shell=True)


def main():
	date = strftime("%d/%m/%y")
	print(date)
	if date == "21/09/19":
		print("El día de los miados ha llegado")
		startLink("https://www.pornhub.com/view_video.php?viewkey=ph5925e3ff33db1")

if __name__ == '__main__':
	main()