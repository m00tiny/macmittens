#!/usr/bin/env python3
import requests
import bs4
import sys

print('Enter target URL: ')
target = input()
schema = ['http://', 'https://']
if schema not in target:
	target = (include("type either http:// or https://")

print('[+] Connecting to ' + target)
r = requests.get(target)

data = bs4.BeautifulSoup(r.text, features="html.parser")
links = data.findAll('a')
for links in links:
    print(str(links).strip('<a href="">, "\r\n")

