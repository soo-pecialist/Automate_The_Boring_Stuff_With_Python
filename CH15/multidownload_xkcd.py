#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:15:21 2019

@author: Soo Hyeon Kim
Downloads XKCD comics using multiple threads.
"""

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic+1):
        # Download the page.
        print("Downloading page http://xkcd.com{} ...".format(url_number))
        res = requests.get('http://xkcd.com/{}'.format(url_number))
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text)
        
        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('Could not find comic image.')
        else:
            comic_url = comic_elem[0].get('src')
            # Download the image.
            print('Downloading image {} ...'.format(comic_url))
            
            try:
                res = requests.get(comic_url)
            except Exception as ecc:
                print('There was a problem: {}'.format(ecc))
            
            try:
                res.raise_for_status()
            except Exception as ecc:
                print('There was a problem: {}'.format(ecc))
            
            # Save the image to ./xkcd.
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()
    
# TODO: Create and start the Thread objects.
download_threads = []       # a list of all the Thread objects
for i in range(0, 1400, 100):       # loops 14 times, creates 14 threads
    download_thread = threading.Thread(target=download_xkcd, args=(i, i+99))
    download_threads.append(download_thread)
    download_thread.start()            
    
# TODO: wait for all threads to end.
for download_thread in download_threads:
    download_thread.join()

print('\nDone.')
