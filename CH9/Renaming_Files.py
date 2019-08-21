#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:36:59 2019

@author: soohyeonkim

Renaming_Files.py - Renames filenames with American mm-dd-yyyy date format
to European dd-mm-yyyy
"""

import shutil, os, re

# TODO: Create a regex that matches files with the American date format
date_patter = re.compile(r"""
                    ^(.*?)           # all text before the date
                    ((0|1)?\d)-      # one or two digits for the month
                    ((0|1|2|3)?\d)-  # oen or two digits for the day
                    ((19|20)\d{2})   # four digits for the year
                    (.*?)$           # all text after the date
                         """, re.X)

# TODO: loop over the files in the working directory
for amer_filename in os.listdir():
    mo = datePattern.search(amer_filename)

    # TODO: skip files without a date
    if mo == None:
        continue

    # TODO: Get the different parts of the filename.
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part    = mo.group(4)
    year_part   = mo.group(6)
    after_part  = mo.group(8)

    # TODO: Form the European-style filename.
    euro_filename = before_part + day_part + '-' \
                   + month_part + '-'           \
                   + year_part + '-'
    
    # TODO: Get the full, absolute file paths
    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filname = os.path.join(abs_working_dir, euro_filename)

    # TODO: Rename the fiels
    print('Renaming "{}" to "{}"...'.format(amer_filename, euro_filename))
#    shutil.move(amer_filename, euro_filename) # uncomment after testing

 
