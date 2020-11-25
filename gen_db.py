#!/usr/bin/env python3

# Only use this script if you know what you're doing. Otherwise, you can rely
# on the updated databases and hashes on the GitHub repository.

import bs4
import json
import re
import sys

def main(ipath, opath):

	print(f"Generating database from {ipath}.")

	data = {}

	with open(ipath, "r") as f:
		tables = bs4.BeautifulSoup(f.read(), "html.parser").find_all("table")

	for table in tables:
		for row in table.find_all("tr")[1::]:
			course = row.find("td")
			if re.match("\d{5}", course.text):
				data[course.text] = course.find("a")["href"]

	with open(opath, "w+") as f:
		json.dump(data, f)

	print(f"Done. Written to {opath}.")

if __name__ == "__main__":
	main(*sys.argv[1:3])
