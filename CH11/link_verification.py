#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:54:21 2019

@author: Soo Hyeon Kim
Given the URL, the program will attempt to download every linked page on the 
page.  The program should flag any pages that have a 404 "Not Found" status 
code and print them out as broken links

"""


import requests
from bs4 import BeautifulSoup

main_url = "https://en.wikipedia.org/wiki/Wikipedia"
errorCode = '404'

res = requests.get(main_url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
link_elems = soup.select('a[href]')

errors = []
print("Validating ... this may take a while. Relax...")

"""
if you want to check unique start of each links, try this:
check = []
for link in link_elems:
    check.append(link.get('href')[:5])

print(set(check)) # this should show the pattern
"""
for link in link_elems:
    url = link.get('href')
    
    if url.startswith("https://"):
        try:
            res = requests.get(url, timeout=0.5)
            res.raise_for_status()
        except Exception as exc:
            if errorCode in str(exc.args[0]):
                print("There was a problem with the url: {}".format(exc))
                errors.append(url)
    
    elif url.startswith("//"):
        try:
            res = requests.get('http:'+url, timeout=0.5)
            res.raise_for_status()
        except Exception as exc:
            if errorCode in str(exc.args[0]):
                print("There was a problem with the url: {}".format(exc))
                errors.append(url)
    
    elif url.startswith("/w"):
        try:
            res = requests.get("https://en.wikipedia.org" + url, timeout=0.5)
            res.raise_for_status()
        except Exception as exc:
            if errorCode in str(exc.args[0]):
                print("There was a problem with the url: {}".format(exc))
                errors.append(url)
    
    else:
        try:
            res = requests.get("https://en.wikipedia.org/wiki/Wikipedia" \
                               + url, timeout=0.5)
            res.raise_for_status()
        except Exception as exc:
            if errorCode in str(exc.args[0]):
                print("There was a problem with the url: {}".format(exc))
                errors.append(url) 
            
print("Done!")
print("{} links were scanned from '{}'".format(len(link_elems), main_url))
print("{} errors of type '404' found".format(len(errors)))
            