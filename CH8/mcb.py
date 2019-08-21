#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:45:03 2019

@author: soohyeonkim
"""

# Usage: mcb.py save <keyword> -> Saves clipboard to keyword
#        mcb.py <keyword> -> Loads keyword to clipboard
#        mcb.py list -> Loads all keywords to clipboard.
#        mcb.py delete <keyword> -> delete a keyword from the shelf
#        mcb.py delete -> delete all keywords from the shelf



import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    
# Delete keyword from the shelf:
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
    
# list keywords, load content, and delete all keywords
elif len(sys.argv) == 2:
    # list keywords
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # load content
    elif sys.arv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    # delete all keyword
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()


mcbShelf.close()