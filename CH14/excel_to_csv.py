#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:06:18 2019

@author: Soo Hyeon Kim
- Reads all the Excel files in the current working directory and outputs 
them as CSV files.
"""

import os, csv, openpyxl


search_dir = './excelSpreadsheets'
for excel_file in os.listdir(search_dir):
    # Skip non-xlsx files, load the workbook object.
    if not excel_file.endswith('.xlsx'):
        continue
    
    csv_folder = os.path.join(os.getcwd(), 'csv_'+os.path.basename(search_dir))
    os.makedirs(csv_folder, exist_ok=True)
    save_folder = csv_folder
    
    wb = openpyxl.load_workbook(os.path.join(search_dir, excel_file), data_only=True)
    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
        
        # Create the CSV filename from the Excel filename and sheet title
        csv_name = os.path.join(save_folder, excel_file[:-5]+'_'+sheet_name+'.csv')
        csv_file = open(csv_name, 'w')
    
        # Create the csv.writer object for this CSV file
        csv_writer = csv.writer(csv_file)
        
        # Loop through every row in the sheet.
        for row_num in range(1, sheet.max_row + 1):
            row_data = []
            # Loop through each cell in the row.
            for col_num in range(1, sheet.max_column + 1):
                # Append each cell's data to row_data
                row_data.append(sheet.cell(row=row_num, column=col_num))
            
            # Write the row_data list to the CSV file
            csv_writer.writerow(row_data)
        
        print("'{}' is created!".format(csv_name))
        
        csv_file.close()

print('\n\nDone! Progoram terminated.')
