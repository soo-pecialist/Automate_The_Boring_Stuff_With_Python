#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:59:16 2019

@author: soohyeonkim
"""

"""
example:
    The ADJECTIVE panda walked to the NOUN and then VERB. 
    A nearby NOUN was unaffected by these events.
    
    -----------
    Enter an adjective:
    silly
    Enter a noun:
    chandelier
    Enter a verb:
    screamed
    Entered a noun:
    pickup truck
    ------------
    
    creates:
    The silly panda walked to the chandelier and then screamed.
    A nearby pickup truck was unaffected by these events.
"""


import re
# get file name and open the template file
file_name = input('Enter template file name: ')
template_file = open(file_name, 'r')
template = template_file.read()

template_file.close() # close file

# print template sentence to the screen
print("\n" + "-"*10 + "Template" + "-"*10 + "\n")
print(template + "\n")
print("-"*28 + "\n")

# find all adj, adv, verb, noun 
regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

# get a list of part of speach in the order
pos = regex.findall(template)

# get an input for them
answers = []
for p in pos:
    if p in ['ADVERB', 'ADJECTIVE']:
        answers.append(input('Enter an {}:\n'.format(p.lower())))
    else:
        answers.append(input('Enter a {}:\n'.format(p.lower())))

# substitute input words for them
for i in range(len(pos)):
    template = re.sub(pos[i], answers[i], template, count=1)

# print new sentence to the screen and save it to a new text file
print("\n" + "-"*10 + "MadLibs" + "-"*10 + "\n")
print(template + "\n")
print("-"*28 + "\n")

# save
save_name = re.search(r'([\w\d_-]+)(.txt)?', file_name).group(1)
save_file = open(save_name+'_Answered.txt', 'w')
save_file.write(template)

save_file.close()