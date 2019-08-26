#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 00:13:02 2019

@author: Soo Hyeon Kim
- a simple countdown script
"""
import time, subprocess

time_left = 60
while time_left > 0:
    print(time_left, end='')
    time.sleep(1)
    time_left -= 1

# TODO: At the end of the countdown, play a sound file
subprocess.Popen(['open', 'alam.wav'], shell=False)
