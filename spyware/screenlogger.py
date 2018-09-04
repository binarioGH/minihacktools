#-*-coding: utf-8-*-
from pyautogui import screenshot
from os import chdir, mkdir
from datetime import date
from time import sleep


if __name__ == '__main__':
	while True:
		try:
			chdir("C:\\{}".format(date.today()))
		except:
			mkdir("C:\\{}".format(date.today()))
		else:
			break
	count = 1
	while True:
		ss = screenshot()
		ss.save("{}-{}.png".format(date.today(),count))
		count += 1
		sleep(5)

