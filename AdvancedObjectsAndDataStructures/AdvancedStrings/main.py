# Advanced Strings
s = "Hello World"

# Changing Case
# Capitalize - first word in a string
print(s.capitalize())

# Upper - changes all case to upper case
print(s.upper())

# Lower - changes all case to lower case
print(s.lower())

# Location and counting methods
# Count - how many of a character in a string
print(s.count('o'))

# Find - find the location of the first occurrence
print(s.find('o'))

# Formatting Methods
# Center method - place your string centered between a provided string of a certain length
print(s.center(20, 'z'))

# Expand tabs
print("hello\thi")

# Other Methods
# Check Case
s = "hello"

# isalnum() - checks if all characters are alphanumeric
print(s.isalnum())

# isalpha() - checks if all characters are alphabetic
print(s.isalpha())

# islower() - checks if all characters are lower
print(s.islower())

# isspace() - checks if all characters are white space
print(s.isspace())

# istitle() - checks if is a title case string
print(s.istitle())

# isupper() - checks if all characters are upper
print(s.isupper())

# endswith() - checks if it ends with character
print(s.endswith('o'))

# Regular Expression Operations
# Split - returns result in a list, separates at all occurrences
print(s.split('e'))

# Partition - search for the separator and return the part before it, the separator itself, and the part after it
print(s.partition('e'))
