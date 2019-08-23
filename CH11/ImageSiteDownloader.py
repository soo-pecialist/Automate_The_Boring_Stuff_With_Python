#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:37:52 2019

@author: Soo Hyeon Kim
program goes to a photo-sharing site like flickr or Imgur, 
searches for a category of photos, and then downloads all 
the resulting images. 
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time, os
import requests


def imgur_image_downloader(keyword='Atlanta'):
    # get a keyword for search
    if keyword == 'Atlanta':
        while True:
            reply = input("Default search keyword is 'Atlanta', you want ot change? (y/n) ")
            if reply == 'y':
                keyword = input("What do you want to search? ")
                break
            elif reply not in ['y', 'n', 'yes', 'no']:
                print("I'm sorry. You must input 'y' or 'n'")
            else:
                print("Okay. Go with no change")
                break

    keyword = keyword.lower()

    # input into search box
    browser = webdriver.Chrome()
    browser.get('https://imgur.com')
    
    search_box = browser.find_element_by_css_selector('input[type=text][class=Searchbar-textInput]')
    search_box.send_keys(keyword + Keys.ENTER)
    time.sleep(1)
    
    url = browser.current_url
    
    res  = requests.get(url)
    res.raise_for_status()
    
    soup = BeautifulSoup(res.text, 'lxml')
    
    # retrieve all image elements
    image_elem = soup.select('.image-list-link img')
    img_urls = ['https:'+img.get('src') for img in image_elem]
    
    print("Start to donload images on {}".format(url))
    file_name = keyword+'_images'
    print("Stored folder name: {}".format(file_name))
    
    # make directory for images
    os.makedirs(file_name, exist_ok=True)
    
    for img_url in img_urls:
        print('Downloading image {} ...'.format(img_url))
        res = requests.get(img_url)
        res.raise_for_status()
        
        with open(os.path.join(file_name, os.path.basename(img_url)), 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
                
#### Test *******             
imgur_image_downloader()
