#-*-coding: utf-8-*-
from win32api import GetAsyncKeyState as gas
from time import sleep

def main():
	while True:
		for i in range(0, 255):
			if gas(i):
				print(chr(i))
				sleep(0.00001)

if __name__ == '__main__':
	main()