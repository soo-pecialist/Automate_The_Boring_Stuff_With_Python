#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:16:04 2019

@author: Soo Hyeon Kim
Identify photo folders on the hard drive
"""

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('/Users/soohyeonkim'):
    num_photo_files = 0
    num_no_photo_files = 0
    for filename in filenames:
        # check if file extension isn't .png or .jpg
        if not (filename.endswith('.jpg') or  filename.endswith('.png')):
            num_no_photo_files += 1
            continue
        
        # Open image file using Pillow
        try:
            im = Image.open(filename)
        except:
            # FileNotFoundError
            continue
        
        width, height = im.size
        
        # Check if width & height are larger than 500
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo
            num_photo_files += 1
        else:
            # Image is too small to be a photo
            num_no_photo_files += 1
        
    # If more than half of files were photo, 
    # print the absolute path of the folder.
    try:
        if num_photo_files / (num_photo_files + num_no_photo_files) > 0.5:
            print(">>> " + os.path.abspath(foldername))
    except:
        ## Zero division error
        continue
        
print('\nDone.')