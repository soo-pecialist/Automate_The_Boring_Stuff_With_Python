#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:41:50 2019

@author: Soo Hyeon Kim
- Find all the CSV files in the current working directory
- Read in the full contents of each file.
- Write out th econtents, skipping the first line, to a new CSV file.
"""

import csv, os

os.makedirs('header_removed', exist_ok=True)

# Loop through every file in the current working directory.
for csv_filename in os.listdir('.'):
    
    if not csv_filename.endswith('.csv'):
        continue 
    
    print("Removing header from " + csv_filename + "...")
    
    # TODO: Read the CSV file in (skipping first row).
    csv_rows = []
    csv_file = open(csv_filename)
    reader = csv.reader(csv_file)
    for row in reader:
        if reader.line_num == 1:
            continue    # skip first row
        csv_rows.append(row)
    csv_file.close()
        
    # TODO: Write out the CSV file.
    directory = os.path.join(os.path.abspath('.'), 'header_removed')
    csv_file = open(os.path.join(directory, 'no_header_'+csv_filename), 'w', newline='')
    csv_writer = csv.writer(csv_file)
    for row in csv_rows:
        csv_writer.writerow(row)
    
    csv_file.close()