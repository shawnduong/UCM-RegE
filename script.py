#!/usr/bin/env python3

import bs4
import multiprocessing
import playsound
import requests
import time

def read_courses() -> list:

	try:
		with open("courses.list", "r") as f:
			courses = [line.strip("\n") for line in f.readlines()]
	except:
		print(":: Error reading courses.list.")
		exit(-1)

	print(":: The following courses will be monitored:")

	for crn in courses:
		print(":: CRN %s" % crn)

	print()

	return courses

def get_course_urls(courses: list) -> dict:

	try:
		with open("page.html", "r") as f:
			data = f.read()
	except:
		print(":: Trouble reading offline catalog.")
		exit(-1)

	soup = bs4.BeautifulSoup(data, "html.parser")

	courses_crns = {}

	links = soup.find_all("a")

	for link in links:
		if link.text in courses:
			courses_crns[link.text] = link["href"]

	return courses_crns

def get_open_seats(url: str) -> str:

	page = requests.get(url).content
	soup = bs4.BeautifulSoup(page, "html.parser")
	table = soup.find_all("table", attrs={"class": "datadisplaytable"})[-1]
	seats = table.find_all("td", attrs={"class": "dddefault"})[-1].text
	opens = True if int(seats) > 0 else False

	if opens:
		seats = "\033[31;1m%s <==\033[0;0m" % seats
		playsound.playsound("alert.ogg")

	return seats

def check_courses(courses: dict) -> None:

	print(":: Checking courses.")
	print(":: TIME: %s" % time.strftime("%d %b %Y @ %H:%M:%S"))

	wPool = multiprocessing.Pool(4)
	seats = wPool.map(get_open_seats, list(courses.values()))
	wPool.close()
	wPool.join()

	c = 0

	for crn in courses.keys():
		print(":: CRN %s: OPEN=%s" % (crn, seats[c]))
		c += 1

	print()

def main() -> None:

	print("Registration Eye (v. Spring 2021)")
	print("Author: Shawn Duong, aka IrisSec skat")
	print("Please see the README.md for setup instructions!")
	print()

	courses = read_courses()
	courses = get_course_urls(courses)

	while True:
		try:
			check_courses(courses)
			time.sleep(10)
		except KeyboardInterrupt:
			print("\r:: Interrupt detected. Exiting.")
			exit(0)

if __name__ == "__main__":
	main()
