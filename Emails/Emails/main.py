# Emails
# "smtplib" library - allows you to send emails
# SMTP (Simple Mail Transfer Protocol Server)
import smtplib
import getpass
import imaplib
import email

# Sending Email with Python
# Create a smtp object
smtp_object = smtplib.SMTP("smtp.gmail.com", 587)

# Establish a Connection
smtp_object.ehlo()

# Initiate Encryption
smtp_object.starttls()

# Generate App Password
email = getpass.getpass("Email: ")

# Hide Password
password = getpass.getpass("Password Please: ")

# Call the Login method
smtp_object.login(email, password)

# Create the Message
from_address = email
to_address = email
subject = input("Enter the subject line: ")
body = input("Enter the body message: ")
message = f"Subject: {subject}\n{body}"

# Send the message
smtp_object.sendmail(from_address, to_address, message)

# Quit/Close Connection
smtp_object.quit()

# Receiving Email with Python
# Use imaplib and email libraries in Python
# imaplib library has special syntax for searching inbox

# Need an imap object
M = imaplib.IMAP4_SSL("imap.gmail.com")

# Need to pass in password and email
# Already gotten above

# Connect to email
M.login(email, password)

# Shows everything you can check in email
M.list()

# Select Inbox
M.select("inbox")

# Search the Inbox
typ, data = M.search(None, 'SUBJECT "NEW TEST PYTHON"')

# Get the Email Data
email_id = data[0]
result, email_data = M.fetch((email_id, '(RFC822'))

# Look at the Email Data
print(email_data)

# Get the Message
raw_email = email_data[0][1]
raw_email_string = raw_email.decode("utf-8")

# Parse String
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
