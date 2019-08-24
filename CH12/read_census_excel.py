#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:46:28 2019

@author: Soo Hyeon Kim
- Reads the data from the Excel spreadsheet
- counts the number of census tracts in each county
- counts the total population of each county
- prints the results
"""

import openpyxl, pprint

print("Opening workbook...")
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

# TODO: Fill in county_data with each county's pop, and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row+1): # starts from row 2 b/c row 1 is header
    # Each row in the spreadsheet has data for one census tract.
    state   = sheet['B' + str(row)].value
    county  = sheet['C' + str(row)].value
    pop     = sheet['D' + str(row)].value
    
    # Make sure the key for this state exists
    county_data.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})
    
    # Each row represents one census tract so increment by one.
    county_data[state][county]['tracts'] += 1
    # Increase the county pop by the pop by the pop in this census tract
    county_data[state][county]['pop'] += int(pop)
    
    
# TODO: Open a new text file and write the contents of county_data to it. 
print('Writing results...')
with open('census2010.py', 'w') as result_file:
    result_file.write('all_data = '+ pprint.pformat(county_data))
print('Done.')
    
#### take a partial view of census2010.py
import census2010
print(list(census2010.all_data.items())[0:2])