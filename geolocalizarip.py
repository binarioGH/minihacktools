#-*-coding: utf-8-*-
from requests import get
from json import loads
from sys import argv


def main():
	if len(argv) == 1:
		ip = ""
	else:
		ip = argv[1]
	api_url = "http://ip-api.com/json/"
	res = get("{}{}".format(api_url, ip))
	content = loads(res.content)
	for key in content:
		print("{} : {}".format(key, content[key]))

if __name__ == '__main__':
	main()