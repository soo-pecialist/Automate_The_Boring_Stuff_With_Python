#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:29:04 2019

@author: Soo Hyeon Kim
- Display the current x- and y-coordinates of the mouse cursor
0 Update these coordinates as the mouse moves around the screen
"""

import pyautogui
print("Press Ctrl-C to quit.")

# TODO: Get and print th emouse coordinates.
try:
    while True:
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
