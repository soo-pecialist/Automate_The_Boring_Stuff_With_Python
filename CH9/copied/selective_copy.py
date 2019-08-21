#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:46:58 2019

@author: soohyeonkim

walks through a folder tree and searches for files with a certain file
extension (e.g., .pdf, .jpg). Copy these files from whatever location 
they are in to a new folder.

"""

import os, re, shutil

def selective_copy():
    # TODO: get current location and show it to a user
    cwd = os.getcwd()
    print("Your current location is {}".format(cwd))
    
    # TODO: Get inputs for root, extension, destination path
    while True:
        root = input("What location do you want to start search from? ").strip()
        if os.path.exists(root): # make sure it is legitimate
            break
        else:
            print("Please input root directory in relative or absolute path")
    
    ext = input("What file format are you looking for? (e.g., .jpg, .txt) ")\
                    .strip().lower()
    
    if not ext.startswith("."): # in case forget putting "."
        ext = "." + ext
    
    while True:
        dest =  input("Where do you want copies located? Please include folder name ")\
                    .strip()
        if os.path.exists(dest): # make sure it exists
            break   # exists
        else:
            # if not, make new one
            try:
                 os.mkdir(dest)
            except OSError: # in case of error
                print ("Creation of the directory %s failed" % dest)
                print("Please input destination in relative or absolute path")
                continue # go get input again
            
            if os.path.exists(dest): # check again if made 
                break
            else: # if not, address is wrong
                print("Please input destination in relative or absolute path")
    
    
    # beware that it can be either relative or absolute path
    # and we need absolute path
    if not os.path.isabs(root): # if relative path
        root = os.path.abspath(root)
    if not os.path.isabs(dest):
        dest = os.path.abspath(dest)
    
    # TODO: make regex pattern
    search_pattern = re.compile(r"^(.*?)"+ext+"$")
    
    # TODO: walk through the folder and detect files and copy to destination
    for foldername, subfolders, filenames in os.walk(root):
        # we don't want hidden folders digged
        if os.path.basename(foldername).startswith("."):
            continue
        
        if os.path.basename(foldername) == os.path.basename(dest):
            continue  # we don't have to copy the copied ones
        
        print("Searching in {}...".format(foldername))
        # go through all files
        for filename in filenames:
            # we don't want hidden files searched
            if filename.startswith("."):
                continue
            
            base = os.path.basename(filename)
            
            if search_pattern.search(base): # if matches
                shutil.copy(filename, dest) # copy to destination
                print("\t{} is copied.".format(base))
    
    print("Done!")

#### test *******    
selective_copy()

