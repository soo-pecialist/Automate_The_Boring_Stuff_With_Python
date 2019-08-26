#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 00:37:20 2019

@author: Soo Hyeon Kim
"""

import time, pyperclip

# Display the program's instructions.
input('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch'
      'Press Ctrl-C to quit. or simply type "q" or "quit"')
print('\nStarted.')
start_time = time.time()
last_time = start_time
lap_num = 1
copy_str = ''
# TODO: Start tracking the lap time.
try:
    while True:
        
        input_ = input()
        lap_time = str(round(time.time() - last_time, 2)).rjust(6)
        total_time = str(round(time.time() - start_time, 2)).rjust(6)
        
        print('Lap #{}: {} ({})'.format(str(lap_num).rjust(2), total_time, lap_time, end=''))
        
        copy_str = copy_str + \
                            'Lap #{}: {} ({})\n'.format(str(lap_num).rjust(2), \
                            total_time, lap_time)
        
        if input_.lower() in ['quit', 'q']:
            break
              
        lap_num += 1
        last_time = time.time()
        
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone. Your result is copied to the clipboard.'
          'If you want to paste it, use ctrl+v')
    
pyperclip.copy(copy_str)