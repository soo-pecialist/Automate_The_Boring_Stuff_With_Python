#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:13:03 2019

@author: Soo Hyeon Kim
Read tex files and insert those contents into a spreadsheet. 
First line of text will be in the cells of column A, Second line column B, 
and so on. 
"""


import openpyxl, re

filename = 'text_file.txt'

wb = openpyxl.Workbook()
sheet = wb['Sheet']


text_file = open(filename, 'r')

text = text_file.read()

## Let's clean text taking symbols out
regex = re.compile(r'[.,-_?!"\']')
text = regex.sub("", text)

text_lines = text.split('\n')
holder = []
for line in text.split('\n'):
    holder.append(line.split())

    
max_col = len(holder)
row_num = 0
col_num = 1

# write to spreadsheet
for col in holder: # col is list

    row_num = len(col)
    for r in range(1, row_num+1):
        sheet.cell(row=r, column=col_num).value = col[r-1]
    
    col_num += 1
    
base = re.findall(r'^([\w\d_]+)\.[\d\w]+', filename)[0]
saved_file = base + '.xlsx'
wb.save(saved_file)

print("'{}' has been created!".format(saved_file))