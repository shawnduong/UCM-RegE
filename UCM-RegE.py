#!/usr/bin/env python3

import json
import os
import time
import vlc

from lib.initialization import *
from lib.scan import *

def main():

	banner()

	if (missing := check_dependencies()):
		print("Packages not found. Please install the following and try again.")
		for pkg in missing: print(pkg)
		return -1

	path = f"{os.path.dirname(os.path.abspath(__file__))}/assets/data/classes.json"

	if ( not os.path.exists(path) ) or ( not checksum_test(path) ):
		print(":: A CRN database was not found or was not up-to-date. The latest database will be downloaded.")
		print()
		download_database(path)

	with open(path, "rb") as f:
		database = json.load(f)

	path = f"{os.path.dirname(os.path.abspath(__file__))}/CRNs.txt"

	if not os.path.exists(path):
		print(":: CRNs.txt was not found. Please enter the CRNs you would like to track:")
		print()
		make_crnlist(path)

	crns = [l.strip("\n") for l in open(path, "r").readlines()]
	data = {crn:database[crn] for crn in crns if crn in database.keys()}

	audpath = f"{os.path.dirname(os.path.abspath(__file__))}/assets/audio/alert.wav"
	player  = vlc.MediaPlayer(audpath)

	while True:

		try:
			check(data, player)
			time.sleep(8)
		except KeyboardInterrupt:
			print("\r:: Interrupt detected. Exiting.")
			exit(0)
		except Exception as e:
			print("\r:: Some other exception detected. Exiting.")
			print(e)
			exit(0)

if __name__ == "__main__":
	main()
