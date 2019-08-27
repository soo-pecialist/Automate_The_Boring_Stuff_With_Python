#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:21:47 2019

@author: Soo Hyeon Kim
Displays the mouse cursor's current position and rgba value. 
"""

import pyautogui, time
print("Press Ctrl-C to quit.")

# TODO: Get and print th emouse coordinates.
try:
    while True:
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixel_color = pyautogui.screenshot().getpixel((x,y))
        position_str += ' RGB: (' + str(pixel_color[0]).rjust(3)
        position_str += ', ' + str(pixel_color[1]).rjust(3)
        position_str += ', ' + str(pixel_color[2]).rjust(3) + ')'
        print(position_str, end='')
        
        time.sleep(0.75) 
        delete = '\b'*len(position_str)
        for d in delete:
            print(d, end='', flush=True)
        time.sleep(0.25) 
        
except KeyboardInterrupt:
    print('\nDone.')

