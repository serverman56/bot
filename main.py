# make a python bot to automate the process of downloading the files from the website

import requests
import os
import time
import sys
import re
import json
import urllib.request
import urllib.parse
import urllib.error

# get the url of the website
url = "http://www.astro.louisville.edu/software/spacepy/"
path = str(os.getcwd()) + '/data/'
filled = False

# get the html of the website
r = requests.get(url)
html = r.text
print(html)