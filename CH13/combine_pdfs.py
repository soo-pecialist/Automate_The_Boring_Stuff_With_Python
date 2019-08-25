#!/usr/bin/env python3
"""
Created on Sat Aug 24 15:47:49 2019

@author: Soo Hyeon Kim
- Find all pdf files in the current working directory
- sort the filenames so the pdfs are added in order
- write an each page, excluding the first page, of each pdf to the output file.
"""

import PyPDF2 as pypdf2
import os

# Get all the PDF filenames
pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)
        
# sort in alphabetical order
pdf_files.sort(key=str.lower)

# to write pdf that merged all pdfs
pdf_writer = pypdf2.PdfFileWriter()

# TODO: loop through all the pdf files
for filename in pdf_files:
    pdf = open(filename, 'rb')
    pdf_reader = pypdf2.PdfFileReader(pdf)

    # TODO: loop through all the pages (except the first) and add them.
    for page_num in range(1, pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)

# TODO: save the resulting PDF to a file.
save_name = 'allminutes.pdf'
with open(save_name, 'wb') as pdf_output:
    pdf_writer.write(pdf_output)

print("Done. {} is created for your sake".format(save_name))