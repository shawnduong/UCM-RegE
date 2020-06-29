# UC Merced Registration Eye

![](./img/example.png)

This is a Python script that helps UC Merced students get the classes they need by alerting them when seats open up. This script works by reading a list of CRNs (course reference numbers) from the `courses.list` file, getting the URLs for the respective courses from the saved `page.html` file (last updated April 2020), and then scraping the online course page to see if there are any open seats. If there are open seats, the program will play a simple alert sound.

It's recommended that you let this run on your computer 24/7 in the background while you do other things. Whenever you hear the alert sound, you can check back on the script to see which class is open. This script requires a stable and constant internet connection. If this is interrupted at any time then the script will not function and you will have to restart it when you regain a connection.

You can read about how this was developed here: https://shawnduong.github.io/Creating-a-Coursicle-Clone-in-Python

## Installation

Installation is fairly simple. Just clone the git repository and run the `script.py` Python script. Make sure that you have the following dependencies installed:

- `bs4`
- `multiprocessing`
- `playsound`
- `requests`
- `time`

## Setup

Replace the sample CRNs in `courses.list` with the CRNs of the courses that you need.

## Testing

This has been tested on a custom Arch Linux system with Python 3.8.2. It is not known whether or not this script will function in another environment such as Windows or Mac OS. Please submit an issue if this script does not work for any reason, complete with a description, error logs, steps to reproduce, and other information you deem relevant.
