#-*-coding: utf-8-*-
from random import choice, shuffle
from sys import argv
from optparse import OptionParser as opt
from selenium import webdriver


class Harasser:
	def __init__(self, url):
		self.url = url
		self.broken = False


	def send_input(self, mail, password):
		driver = webdriver.Chrome()
		try:
			driver.get(self.url)
			driver.find_element_by_name("idfb").send_keys(mail)
			driver.find_element_by_name("pass").send_keys(password)
			driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
		except:
			self.broken = True
		finally:
			driver.close()

	def generate_fake_credentials(self):
		return (self.genran(mail=True), self.genran())
		

	def genran(self, mail=False):		
		abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789.")
		my = abc.copy()
		shuffle(my)
		my = "".join(my)
		if mail:
			extra = ("@gmail.com", "@hotmail.com", "@yahoo.com", "@bigbro.com")
			my += choice(extra)
		return my

	def harass(self, rnge=1000):
		for i in range(0, rnge+1):
			if i%10 == 0 and i != 0:
				print("[{}] fake credentials sent.".format(i))
			if self.broken:
				print("[-]Broken url :(")
				break
			user, passw = self.generate_fake_credentials()
			self.send_input(user, passw)


def main():
	op = opt("Usage: %prog [flags] [values]")
	op.add_option("-u", "--url", dest="url", default="none", help="Set the phishing url")
	op.add_option("-r", "--range", dest="range", type="int", default=1000, help="Set a total of fake credentials that are going to be sent.")
	(o, argv) = op.parse_args()
	if o.url == "none":
		print("[-]The url wasnt set.")
	har = Harasser(o.url)
	har.harass(o.range)



if __name__ == '__main__':
	main()