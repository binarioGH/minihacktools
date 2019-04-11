#-*-coding: utf-8-*-
from random import shuffle
ABC = "abcdefghijklmnopqrstuvwxyz"

def generateKey(it = 0):
	abcs = [list(ABC)];
	key = ""
	for l in range(it):
		abcs.append(abcs[0].copy);
	for a in abcs:
		shuffle(a);
		key += "".join(a);
	return key;

def inAbc(l, abc):
	if(l in abc):
		return True
	return False

def isLower(l):
	return inAbc(l, ABC);

def isAlpha(l):
	return inAbc(l, ABC.upper());


class Vigenere:
	def __init__(self, key ,abc=ABC):
		self.key = key;
		self.abc = abc;

	def encrypt(self, msj):
		return self.translate(msj, "e");

	def decrypt(self,msj):
		return self.translate(msj, "d");

	def translate(self,msj, m):
		translated = "";
		msj = str(msj);
		currentIndex = 0;
		abcIndex = 0;
		keyIndex = 0;
		keyIt = 0;
		addChar = "";
		for char in msj:
			abcIndex = self.abc.find(str(char).lower());
			keyIndex = self.abc.find(self.key[keyIt]);
			if(abcIndex != -1):
				if(m == "d"):
					keyIndex *= -1;
				currentIndex = abcIndex + keyIndex;
				if(currentIndex >= len(self.abc)):
					currentIndex %= len(self.abc);
				if(currentIndex < 0):
					currentIndex += len(self.abc)
				addChar = self.abc[currentIndex];
				if(isAlpha(char)):
					addChar = addChar.upper();
			else:
				addChar = char;

			translated += addChar;
			if(keyIt >= len(self.key)-1):
				keyIt = 0;
			else:
				keyIt += 1;

		return translated;
	