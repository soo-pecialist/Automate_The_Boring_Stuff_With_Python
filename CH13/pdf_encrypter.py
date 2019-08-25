#!/usr/bin/env python3
"""
Created on Sat Aug 24 22:22:21 2019

@author: Soo Hyeon Kim
Finds all pdfs in a folder and encrypt th epdfs using a password provided 
on the command line with '_encrypted.pdf' suffix added to the original file. 
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



encrypt_failed = [] # in case failure

for folder, subfolders, filenames in os.walk(root):
    
    for filename in filenames:
        if filename.endswith('.pdf'):
            path = os.path.join(folder, filename)
            path_ = open(path, 'rb')
            try:
                pdf_reader = pypdf2.PdfFileReader(path_)
            except:
                continue
            
            # file shouldn't be encrypted to be read
            if not pdf_reader.isEncrypted:
                pdf_writer = pypdf2.PdfFileWriter()
                for page_num in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))
                
                # Encrypt copy of pdf and save with _encrypted suffix
                pdf_writer.encrypt(password)
                encrypted_path = path[:-4] + '_encrypted.pdf'
                encrypted_version = open(encrypted_path, 'wb')
                
                pdf_writer.write(encrypted_version)
                encrypted_version.close()
                
                # check file was encrypted properly
                encrypted_path_ = open(encrypted_path, 'rb')
                pdf_reader2 = pypdf2.PdfFileReader(encrypted_path_)
                if (pdf_reader2.isEncrypted) \
                        and (pdf_reader2.decrypt(password)):
                    os.remove(path)
                else:
                    encrypt_failed.append(filename)
                
            path_.close()
            
if encrypt_failed:
    print("The following files failed their encryption checks and were"
          " not deleted: ")
    for filename in encrypt_failed:
        print(filename)
else:
    print("All PDF's in the folder tree have been successfully encrypted.")
    print("Original files are deleted")