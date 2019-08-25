#!/usr/bin/env python3
"""
Created on Sat Aug 24 23:41:21 2019

@author: Soo Hyeon Kim
Finds all pdfs in a folder and deencrypt th epdfs using a password provided 
on the command line with '_decrypted.pdf' suffix removed to the original file. 
Get rid of original files in the end. 
"""

import os, sys
import PyPDF2 as pypdf2

try:
    password = sys.arg[1].strip()
except:
    password = input("You haven't provided password. What is it? ").strip()


while True:
        root = input("What location do you want to search through?").strip()
        root = os.path.abspath(root)
        
        if os.path.exists(root): # make sure it is legitimate
            break
        else:
            print("Please input root directory in relative or absolute path")



decrypt_failed = [] # in case failure

for folder, subfolders, filenames in os.walk(root):
    
    for filename in filenames:
        if filename.endswith('.pdf'):
            path = os.path.join(folder, filename)
            path_ = open(path, 'rb')
            try:
                pdf_reader = pypdf2.PdfFileReader(path_)
            except:
                continue

            if pdf_reader.isEncrypted is True:
                if not pdf_reader.decrypt(password):
                    print(filename + ' failed to decrypt.')
                    decrypt_failed.append(filename)
                else:
                    pdf_writer = pypdf2.PdfFileWriter()
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))

                    # Encrypt copy of PDF and save with _encrypted suffix
                    decrypted_path = path[:-4] + '_decrpyted.pdf'
                    decrypted_version = open(decrypted_path, 'wb')
                    pdf_writer.write(decrypted_version)
                    decrypted_version.close()

if decrypt_failed != []:
    print("All encrypted PDF's, except those listed above, were "
          "decrypted successfully. All of the original files have been kept.")
else:
    print("All encrypted PDF's in the folder tree were decrypted successfully. "
          "The original files have been kept.")
