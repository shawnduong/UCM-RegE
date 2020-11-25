def get_seats(url):

	import bs4
	import requests

	page = requests.get(url).content
	soup = bs4.BeautifulSoup(page, "html.parser")

	table = soup.find_all("table", attrs={"class": "datadisplaytable"})[-1]
	seats = table.find_all("td", attrs={"class": "dddefault"})[-1].text

	return seats

def check(data, player):

	import multiprocessing
	import os
	import time

	print(":: Checking courses.")
	print(f":: TIME: {time.strftime('%d %b %Y @ %H:%M:%S')}")

	wPool = multiprocessing.Pool(4)
	seats = wPool.map(get_seats, list(data.values()))
	wPool.close()
	wPool.join()

	crns = [k for k in data.keys()]

	for i in range(len(crns)):
		print(f":: CRN {crns[i]}: OPEN={seats[i]}")

	if max([int(i) for i in seats]) > 0:
		player.play()
		time.sleep(2)
		player.stop()

	print()

