#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:31:34 2019

@author: Soo Hyeon Kim
- update 'resize_and_add_logo.py' to do:
    - add bmp & gif
    - be case insensitive to extension
    - make sure image is at least twice the width and height of the logo image
      Otherwise, should skip adding the logo.
"""

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_img = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_img.size
prop = 1/logo_width

## logo needs to be smaller
logo_width = int(90 * logo_width * prop)
logo_height = int(90 * logo_height * prop)

logo_img = logo_img.resize((logo_width, logo_height))

# TODO: Loop over all files in the working directory
os.makedirs('updated_with_logo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    
    if not filename[-4:].lower() in ['.png', '.jpg', '.bmp', '.gif'] \
        or filename == LOGO_FILENAME:
        continue       # skip non-image files and the logo file itself
    
    img = Image.open(filename)
    width, height = img.size

    # TODO: Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
            
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
    
        # Resize the image.
        print('Resizing {} ...'.format(filename))
        img = img.resize((width, height))

    if not ((width > 2 * logo_width) and (height > 2 * logo_height)):
        continue
    
    # TODO: Add the logo
    print('Adding logo to {} ...'.format(filename))
    img.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

    # TODO: Save changes. 
    img.save(os.path.join('updated_with_logo', filename))

