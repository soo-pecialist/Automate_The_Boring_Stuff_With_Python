#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:49:49 2019

@author: Soo Hyeon Kim

takes an email address and string of text on the command line and, 
logs into your email account and sends and email of the string to 
the provided address.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass, time

def command_line_emailer():
    welcome = """
    Welcome to emailer program! This program will help you send
    an email on terminal without opening your web browser. We will
    need your gmail address, receiver's email address, your password,
    subject, and message."""
    print(re.sub(" +", " ", welcome.replace('\n', '')).strip())
    print()
    
    sender = input("What is your google email address? ")
    receiver = input("What is receiver's email address? ")
    password = getpass.getpass('Password (shows as *): ')
    print()
    subject = input("Enter your email subject: " )
    print("Please type your message below. When done type 'SEND' or 'send':\n")
    
    lines = []
    while True:
        line = input()
        if line.lower() != 'send':
            lines.append(line)
        else:
            break
    
    message = '\n'.join(lines)
    
#    print(sender, receiver, password)
#    print(message)
    
    # open a browser and log into your email
    browser = webdriver.Chrome()
    browser.get('https://gmail.com')
    
    email_elem = browser.find_element_by_css_selector('#identifierId')
    email_elem.send_keys(sender)
    
    next_button_elem = browser.find_element_by_css_selector("div[role=button]")
    next_button_elem.click()
            
    
    time.sleep(1.5) # page open delay
    
    password_elem = browser.find_element_by_css_selector("input[type=password]")
    password_elem.send_keys(password)

    password_elem.send_keys(Keys.RETURN)
    
    time.sleep(1.5) # page open delay
    
    # let's compose email
    compose_elem = browser.find_element_by_css_selector('.z0 div[role=button]')
    compose_elem.click()
    
    # recipient 
    time.sleep(1.5) # page open delay
    receiver_elem = browser.find_element_by_name('to')
    receiver_elem.send_keys(receiver)
    time.sleep(1)
    
    # subject
    subject_elem = browser.find_element_by_name('subjectbox')
    subject_elem.send_keys(subject)
    time.sleep(1)
    
    # message
    subject_elem.send_keys(Keys.TAB + message)
    time.sleep(1)
    
    # sent!
    subject_elem.send_keys(Keys.TAB +Keys.TAB + Keys.ENTER)

    
                                                      
if __name__ == "__main__":
    command_line_emailer()