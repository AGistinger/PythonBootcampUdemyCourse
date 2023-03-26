# CSV
# Comma separated variables, Raw data from spreadsheet
# Pandas - Full data analysis library
# Openpyxl - Designed for Excel files, retains Excel functionality
# python-excel.org tracks various Excel based Python libraries
# Google Sheets Python API
import csv

# Get Data From CSV File
# Open the file with an encoding
data = open("C:\\Users\\gistadr\\Documents\\PythonUdemyBootcamp\\PDFsAndSpreadsheets\Files\\example.csv", encoding="utf-8")

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)
print(data_lines)

# Read in data
print(data_lines[0])  # shows column information
print(len(data_lines))

# Go up to row 5
for line in data_lines[:5]:
    print(line)

# Get user email
print(data_lines[0][3])

# Go through every row and get the email
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])

print(all_emails)

full_names = []
for line in data_lines[1:]:
    full_names.append(line[1] + " " + line[2])

print(full_names)

# Write Data To CSV File
file_to_output = open("C:\\Users\\gistadr\\Documents\\PythonUdemyBootcamp\\PDFsAndSpreadsheets\\Files\\to_save_file.csv", mode='w', newline="")
csv_writer = csv.writer(file_to_output, delimiter=",")

csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])

file_to_output.close()

f = open("C:\\Users\\gistadr\\Documents\\PythonUdemyBootcamp\\PDFsAndSpreadsheets\\Files\\to_save_file.csv", mode='a', newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(['f', 'j', 'k'])
f.close()
