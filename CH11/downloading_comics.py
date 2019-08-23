#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:01:58 2019

@author: Soo Hyeon Kim
- loads the XKCD home page.
- Saves the comic image on the page
- Follows the Prvious Comic link
- Repeats until it reaches the first comic
"""

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # TODO: Donload the page.
    print('Downloading page {}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    
    # TODO: Find the URL of the comic image
    comic_elem = soup.select('#comic img') #inside <div> w/ id=comic, img
    if comic_elem == []:
        print("Couldn't find comic image.")
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        # Download the image.
        print('Downloading image {}...'.format(comic_url))
        
        try:
            res = requests.get(comic_url)
        except Exception as ecc:
            print('There was a problem: {}'.format(ecc))
            
        try:
            res.raise_for_status()
        except Exception as ecc:
            print('There was a problem: {}'.format(ecc))
    
        # TODO: Save the image to ./xkcd
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        
            
    # TODO: Get the Prev button's url
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')
    
    
print('Done.')