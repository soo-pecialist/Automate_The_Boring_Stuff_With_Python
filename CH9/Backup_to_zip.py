#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:32:13 2019

@author: soohyeonkim

Copies an entire folder and its content into a ZIP file whose filename
increments
"""

import zipfile, os

def backup_to_zip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder) # make surefolder is absolute
    
    # Figure out the filename this code should use based on
    # what files already exist
    number = 1
    while True:
        zip_filename = os.path.basename(folder) \
                            + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1
    
    # Create the ZIP file
    print('Creating {}...'.format(zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    
    # Walk the entire folder tree and compress the files in each folder. 
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in {}...'.format(foldername))
        # Add the current folder to the zip file.
        backup_zip.write(foldername)
        # Add all the files in this folder to the zip file.
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue    # Don't back up the backup zip files
            
            backup_zip.write(os.path.join(foldername, filename))
        
    backup_zip.close()
        
    print('Done.')
        
