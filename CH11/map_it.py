#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:44:01 2019

@author: Soo Hyeon Kim
Launches a map in the browser using an address from command line or clipboard.
"""

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)

## try below
## 1)
## !python3 map_it.py 870 Valencia St, San Francisco, CA 94110
## 2) 
## copy: 870 Valencia St, San Francisco, CA 94110