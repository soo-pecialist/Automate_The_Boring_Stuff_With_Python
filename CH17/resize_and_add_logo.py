#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:03:47 2019

@author: Soo Hyeon Kim
- load the logo image
- loop over all .png and .jpg files in the working directory
- check whether the image is wider or taller than 300 pixels
- If so, reduce the width or height(whichever is larger) to 300 pixels and
  scale down the othe rdimension proportionally.
- Paste the logo image into the corner
- Save the altered images to another folder
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
os.makedirs('with_logo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
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
           
    # TODO: Add the logo
    print('Adding logo to {} ...'.format(filename))
    img.paste(logo_img, (width - logo_width, height - logo_height), logo_img)

    # TODO: Save changes. 
    img.save(os.path.join('with_logo', filename))

