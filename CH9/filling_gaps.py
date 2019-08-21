#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:58:25 2019

@author: Soo Hyeon Kim

With a given prefix, such as spam001.txt, spam003.txt, adn so on. in a single
folder and locates any gaps in the numbering. The program will rename all 
the later files to close this gap
"""

import os, re, shutil

# TODO: get a parameter that determines adjust or add between gaps, 
#       Also, weather save file or not

def filling_gaps(cwd=os.getcwd(), adjust=True):
   
    cwd = os.path.abspath(cwd) # make sure cwd is absolute path
    prefix = input("What is the prefix? ")
    
    # group 1: all
    # group 2: numbering
    # group 3: extension
    regex_pattern = re.compile(\
                    "(" + prefix  + "[._\-\s]?([\d]+))(\.[\d\w]+)$")
     
    # TODO: walk through a folder       
    file_list = os.listdir()
    numberings = []
    
    if file_list: # if not empty listextension = found[0][2]
        i = 0
        for file in file_list:
            # TODO: find numbering files with regex pattern
            found = regex_pattern.findall(file)
            
            if found:
                # TODO: Extract all numbers in numbering part in order
                numberings.append(found[0][1])
                if i == 0:
                    extension = found[0][2] # extract extension
#                    print(found)
#                    print(extension)
                    i = 1 # to repeat extrating extension            
            
    else:
        print("Empty folder. Nothing to show")
        return # terminate the program
    
    if not numberings:
        print("No search result. Bye")
        return 
    
    # sort in ascending order of value
    numberings.sort(key=lambda x: int(x))
    # for now for convinience convert spamto int
    numberings = [int(number) for number in numberings]
    min_num = min(numberings)
    max_num = max(numberings)
    # numbers not in numberings. i.e., complement set of numberings
    numberings_c = [x for x in range(min_num, max_num) \
                                        if x not in numberings]
    if not numberings_c:
        print("All seems right")
        return 
    
    min_gap = min(numberings_c) # minimum gap value
    
    ## let's make hashable dictionary {original: 'right form'}
    length_of_out = len([x for x in numberings if x > min_gap])
    added_numbers = list(range(min_gap, min_gap + length_of_out))
    numberings_adj = [x for x in numberings if x < min_gap] + added_numbers
    # to unify format
    numberings_str = ['0'*(len(str(max(numberings_adj))) - \
                           len(str(int(num)))) \
                       + str(num) for num in numberings_adj]
    # dictionary for search
    numberings_dict = {k:v for k, v in zip(numberings, numberings_str)}
    
    min_gap_str = '0' * (len(numberings_str[0]) - len(str(min_gap))) \
                    + str(min_gap)
    
    
    # TODO: check if it is adjust mode or add mode
    if adjust:
        # TODO: if adjust mode, 
        #       re-organize the order in ascending order from min_gap
        file_list.sort(key= lambda x: len(x)) # in order not to overwrite already renamed one
        print(file_list)
        
        for file in file_list:
            # TODO: find numbering files with regex pattern
            found = regex_pattern.findall(file)
            
            if found:
                
                # adjust name in uniform format
                num_str = numberings_dict[int(found[0][1])]
#                print(numberings_dict, found, prefix + num_str + found[0][2])
                # rename
                shutil.move(\
                        os.path.join(cwd, file), \
                        os.path.join(cwd, prefix + num_str + found[0][2])\
                            )
        print("Done adjusting!")
    
    else:
        # TODO: if add mode, add numbering from min_gap
        print("I suggest you save file as '{}'"\
              .format(prefix+min_gap_str+extension))
       
      
#### test *******
print("before renaming")
print(os.listdir('./some'))
filling_gaps(cwd='./some', adjust=True)
print("after renaming")
print(os.listdir('./some'))
        
