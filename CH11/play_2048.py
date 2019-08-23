#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:53:29 2019

@author: Soo Hyeon Kim

# http://gabrielecirulli.github.io/2048
Let program play 2048 own its on. 
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, time

def play_2048(rounds=100):
    print("Let's play 2048. Default round number is {}.".format(rounds))
    reply = input("You want to change it? (y/n) ")
    
    # set round
    while reply != "n":
        rounds = input("How many rounds? ")
        try:
            rounds = int(rounds)
        except:
            print("Hey, type number")
            continue
    
        reply = 'n'
            
    browser = webdriver.Chrome()
    browser.get("http://gabrielecirulli.github.io/2048")
    html_elem = browser.find_element_by_tag_name('html')
    
    while rounds > 0:
        arrow = random.choice([Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT])
        html_elem.send_keys(arrow)
        rounds -= 1
        time.sleep(0.25)
    
    print("Game Over")
        

#### Test *****
play_2048()
