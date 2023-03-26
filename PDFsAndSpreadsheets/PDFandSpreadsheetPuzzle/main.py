# PDFs and Spreadsheets Puzzle Exercise
# You will need to work with two files for this exercise to solve
# the following tasks:
#   * Task One: Use Python to extract the Google Drive link from
#   the .csv file.  (Hint: Its along the diagonal from top left
#   to bottom right).
#   * Task Two: Download the PDF from the Google Drive link and
#   find the phone number that's in the document

import csv
import PyPDF2
import re

files_loc = "C:\\Users\\gistadr\\Documents\\PythonUdemyBootcamp\\PDFsAndSpreadsheets\\Files\\"

# Open the CSV file with "utf-8" encoding
data = open(files_loc + "find_the_link.csv", encoding="utf-8")

# Create a csv reader
csv_data = csv.reader(data)

# Check out the data
data_lines = list(csv_data)

# Get the link from the list of list data
link_str = ""

# Data is the row, Row number is the current row we are on
# using for indexing.  using enumerate for data_lines to
# make it an iterable object
for row_num, data in enumerate(data_lines):
    link_str += data[row_num]

print(link_str)

# Open the PDF with "rb" read binary
f = open(files_loc + "Find_the_Phone_Number.pdf", "rb")

# Read the PDF file
pdf = PyPDF2.PdfReader(f)

# Check the pages
print(len(pdf.pages))

# Regex for phone number
regex = r"\d{3}\D\d{3}\D\d{4}"

# Get all the text in the document
all_text = ""
for n in range(len(pdf.pages)):
    page = pdf.pages[n]
    page_text = page.extract_text()

    all_text += " " + page_text

print(all_text)

# Look for the phone number
for match in re.finditer(regex, all_text):
    print(match.group())
