# PDF
# Portable Document Format
# Many PDFs are not machine-readable through Python
# PyPDF2 library - open source and free
import PyPDF2

files_loc = "C:\\Users\\gistadr\\Documents\\PythonUdemyBootcamp\\PDFsAndSpreadsheets\\Files\\"

# Read in File with "rb" as the mode
f = open(files_loc + "Working_Business_Proposal.pdf", 'rb')

# Use PDF file reader on the file
pdf_reader = PyPDF2.PdfReader(f)

# Confirm the number of pages
print(len(pdf_reader.pages))

# Check if it worked by getting the page
page_one = pdf_reader.pages[0]

# Get the page one object and extract text as String
page_one_text = page_one.extract_text()

# Create new file, Write a new PDF file
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one)
pdf_output = open(files_loc + "Some_BrandNew_Doc.pdf", "wb")
pdf_writer.write(pdf_output)

# Grab all text in a PDF and use a for loop
pdf_text = []

for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())

print(pdf_text[0])

# Close the file
f.close()
pdf_output.close()
