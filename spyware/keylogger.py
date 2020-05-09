#-*-coding: utf-8-*-
from win32api import GetAsyncKeyState as gas
from time import sleep

def main():
	text = ""
	while "Z" not in text:
		for i in range(0, 255):
			if gas(i):
				text += chr(i)
			sleep(0.0000000000000000000001)
	print(text)

if __name__ == '__main__':
	main()

