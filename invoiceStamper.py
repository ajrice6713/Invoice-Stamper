#! python3

# name: invoiceStamper.py
# description: Puts the company invoice Stamp onto a .pdf file
# author: Andrew Rice
# date: 5/20/2019
# version: 1.0
# usage: python invoiceStamper.py
# notes:
# python_version: 3.7.3
# copyright 2019 by Andrew Rice
# source: https://stackoverflow.com/a/31707039

from tkinter import *
from tkinter import filedialog
import os
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

# c = canvas.Canvas('watermark.pdf')
# c.drawImage('STAMP.jpg', 270, 250)
# c.save()
watermark = PdfFileReader(open('U:\\Python Projects\\Invoice Stamper\\watermark.pdf', 'rb'))
output_file = PdfFileWriter()

# Get the invoice location from the user using tkinter
invoice = filedialog.askopenfilename(initialdir=desktop,
                                     title='Select Invoice',
                                     filetypes=(('PDF Files', '*.pdf'), ('all files', '*.*')))

# change this to use the invoice variable
input_file = PdfFileReader(open(invoice, 'rb'))
page_count = input_file.getNumPages()

# Insert the invoice stamp .jpg
for page_number in range(page_count):
    print("Stamping page {} of {}".format(page_number + 1, page_count))
    # merge the watermark with the page
    input_page = input_file.getPage(page_number)
    input_page.mergePage(watermark.getPage(0))
    # add page from input file to output document
    output_file.addPage(input_page)

# Save the invoice pdf to its original location
with open(desktop + '\\stamp_inv.pdf', "wb") as outputStream:
    output_file.write(outputStream)
