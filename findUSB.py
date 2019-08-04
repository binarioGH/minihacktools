#-*-coding: utf-8-*-
from os import getcwd, chdir
OD = getcwd() #OD == original dir
def detect_usb():
	unitlist = ["E:", "D:", "F:"]
	foundUnits = []
	for unit in unitlist:
		try:
			chdir(unit)
		except:
			pass
		else:
			chdir(OD)
			foundUnits.append(unit)
	return foundUnits

def main():
	lastlist = []
	while True:
		newunits = detect_usb()
		if newunits != lastlist:
			lastlist = newunits
			print("Uppdate: {}".format(newunits))
	detect_usb()

if __name__ == '__main__':
	main()