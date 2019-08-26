#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:15:18 2019

@author: Soo Hyeon Kim
A simple stopwatch program.
"""

import time

# Display the program's instructions.
input('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch'
      'Press Ctrl-C to quit. or simply type "q" or "quit"')
print('\nStarted.')
start_time = time.time()
last_time = start_time
lap_num = 1

# TODO: Start tracking the lap time.
try:
    while True:
        
        input_ = input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Lap #{}: {} ({})'.format(lap_num, total_time, lap_time, end=''))
        
        if input_.lower() in ['quit', 'q']:
            break
              
        lap_num += 1
        last_time = time.time()
        
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    