#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 00:23:34 2019

@author: Soo Hyeon Kim
Finding a single english password. 
"""

import PyPDF2, os

print('Enter the directory of the PDF you wish to break:')
file = input()
file = os.path.abspath(file)

with open('dictionary.txt') as f:
    words = f.readlines()

    pdf_reader = PyPDF2.PdfFileReader(open(file, 'rb'))

    for word in words:
        word = word.strip()
        lower = word.lower()
        upper = word.upper()
        if pdf_reader.decrypt(lower) == 1:
            print('Password = ' + lower)
            break
        elif pdf_reader.decrypt(upper) == 1:
            print('Password = ' + upper)
            break