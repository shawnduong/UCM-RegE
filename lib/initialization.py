def banner():

	print("+-------------------------------------------------+")
	print("| UC Merced Registration Eye v2.1                 |")
	print("| Compatible with Spring 2021 registration.       |")
	print("| Source: https://github.com/shawnduong/UCM-RegE/ |")
	print("| Author: https://shawnd.xyz/                     |")
	print("+-------------------------------------------------+")
	print()
	print("v2.1 changelog:")
	print("- Fixed a whitespace in CRN bug.")
	print()

def check_dependencies():

	import pkg_resources

	dependencies = {"beautifulsoup4", "python-vlc", "requests"}

	if len((missing := dependencies - {p.key for p in pkg_resources.working_set})):
		return missing
	else:
		return None

def checksum_test(path):

	import hashlib
	import requests

	sha1 = hashlib.sha1()

	with open(path, "rb") as f:
		while len(chunk := f.read(65536)) > 0:
			sha1.update(chunk)

	data = requests.get("https://raw.githubusercontent.com/shawnduong/UCM-RegE/master/assets/data/sha1sum").content.decode("utf-8").strip("\n")

	return data == sha1.hexdigest()

def download_database(path):

	import requests

	with open(path, "wb+") as f:
		f.write(requests.get("https://raw.githubusercontent.com/shawnduong/UCM-RegE/master/assets/data/classes.json").content)

def make_crnlist(path):

	import re

	data = ""

	while True:

		if (crn := input("Enter a CRN (x to finish): ").replace(" ", "")) == "x":
			break
		elif re.match("\d{5}", crn):
			data += f"{crn}\n"
		else:
			print("Invalid CRN, try again.")

	with open(path, "w+") as f:
		f.write(data)

