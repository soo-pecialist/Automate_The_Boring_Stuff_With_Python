#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:23:36 2019

@author: Soo Hyeon Kim

- Get search keywords from the command line arguments
- Retrieve the search results page
- Open a browser tab for each result
"""

import requests, sys, webbrowser
from bs4 import BeautifulSoup

def open_for_me():
    
    arg=input("Your search phrase? ")
    
    print('Googling...')    # display text while downloading the Google page
    res = requests.get('https://www.google.com/search?q=' + ' '.join(arg))
    
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: {}'.format(exc))
        
    # TODO: Retrieve top search result links
    soup = BeautifulSoup(res.text, 'lxml')
    
    # Open a browser tab for each result
    link_elems = soup.select('.r a')
    num_open = min(5, len(link_elems))
    for i in range(num_open):
        webbrowser.open('http://google.com' + link_elems[i].get('href'))
    