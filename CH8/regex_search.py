#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:05:38 2019

@author: soohyeonkim
"""

import re, os

# get current (present) working directory
pwd = os.getcwd()
# get list of files in the directory
file_list = os.listdir(pwd)
# get list of .txt files
txt_list = re.findall(r'([\w\d_-]+.txt)', " ".join(file_list))

# sample: \s([\d\w]+)\.
user_input = input("Type your regular expression:\n") 

founds = [] # result holder       
#### return including sentences ver.
# loop through all .txt files
for txt in txt_list:
    # open files
    file = open(txt, 'r')
    # read file in one string including space, newline
    search_txt = file.read()
    # strip spaces on the left and right & split sentence on newlien or period
    search_txt_list = \
                re.split(r'(?:\n|\.)',search_txt.strip())[:-1]
    # put '.' back on
    search_txt_list = [line + '.' for line in search_txt_list]
    
    # loop through the sentences
    for line in search_txt_list:
        # filter out biproduct of re.split. 
        if line != ' .':
            # does line has corresponding part to regex expression
            has_it = re.findall(user_input, line)
            if has_it: #if exists
                # add line to founds
                founds += [line.strip() + "({})".format(has_it)]
    file.close()

# coudn't find anything    
if not founds:
    print("Can't find the pattern. Sorry")
# there are the found
else:
    print("Search results:")
    for elem in founds:
        print(' * ' + elem)


#### return words ver.
#for txt in txt_list:
#    file = open(txt, 'r')
#    search_txt = file.read()
#    found = re.findall(user_input, search_txt)
#    print(found)
#    if found:       # if not None
#        founds += found 
#        print(founds)
#    file.close()
#    
#if not founds:
#    print("Can't find the pattern. Sorry")
#else:
#    print("Search results:")
#    for elem in founds:
#        print(' * ' + elem)