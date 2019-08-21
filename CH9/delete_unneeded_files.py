#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:01:30 2019

@author: soohyeonkim

walks through a folder tree and searches for exceptionally large files or 
folders - say, once that have a file size of more than 100MB. 
Print these files with their absolute path to the screen
"""

import os

def detect_unneeded_files(cwd = os.getcwd(), cutoff=100):
    print("Search start from " + os.path.abspath(cwd))
    print("It will show files larger than {}MB".format(cutoff))
    print()
    
    cutoff = cutoff * 10**6  # convert in byte
    founds = []
    
    # TODO: walk through a folder
    for foldername, subfolders, filenames in os.walk(cwd):
        # TODO: skip small folders to save time
        if os.path.getsize(foldername) <= cutoff:
            continue
        
        # TODO: print where you are to the screen in absolute path
        foldername = os.path.abspath(foldername)
        print("  Searching in {} ...".format(foldername))
        
        # TODO: search for large files/folders
        count = 0
        for filename in filenames:
            if os.path.getsize(filename) >= cutoff:
                filename = os.path.abspath(filename)
                founds += [filename]
                count += 1
        print("\tFound {} files!".format(count))
    
    # TODO: print large files to screen
    print("\n---- results ----")
    for i in range(len(founds)):
        print(" [{}] ".format(i+1) + founds[i])
    

#### TEST ************ 
detect_unneeded_files(cutoff=0.0001)