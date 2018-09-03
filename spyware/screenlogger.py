#-*-coding: utf-8-*-
from pyautogui import screenshot
from os import chdir, mkdir
from datetime import date
from time import sleep


if __name__ == '__main__':
	newdir = str(date.today())
	chdir("C:\\")
	mkdir(newdir)
	chdir(newdir)
	count = 1
	while True:
		ss = screenshot()
		ss.save("{}-{}.png".format(date.today(),count))
		count += 1
		sleep(5)

