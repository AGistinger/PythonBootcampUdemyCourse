# Advanced Python Modules
"""
Collections Module
Specialized container types
Alternatives to Python containers
"""
from collections import Counter
from collections import defaultdict
from collections import namedtuple
import os
import shutil
import send2trash
import datetime
from datetime import datetime
from datetime import date
import math
import random
import pdb  # Python Debugger
import re  # regex
import time
import timeit
import zipfile


my_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4]
# Counts the number of unique elements in the list
print(Counter(my_list))

# Counter is a dictionary subclass
my_list = ['a', 'a', 10, 10, 10]
print(Counter(my_list))

print(Counter("aaaaabbbbcccc"))

sentence = "How many times does each word show up in this sentence with a word"
print(Counter(sentence.split()))

# Patterns
letters = "aaaabbbbbccccccdddddddd"
c = Counter(letters)
print(c)
# Returns the most common as a tuple, takes a arg for
# the amount of most common
print(c.most_common(2))

# Will get a list of all unique keys
print(list(c))

# Default Dictionary
d = {'a': 10}
print(d)

# The Default Dictionary will assign a default value if
# there is an instance where a key error would occur
# you need to assign the default value with a lambda expression
d = defaultdict(lambda: 0)
d["correct"] = 100
d["Wrong Key!"]
print(d)

# Named Tuple
my_tuple = (10, 20, 30)
print(my_tuple[0])

# Named Tuple has two main parameters a type name
# and a list of field names (kind of like attributes)
# This allows you to create instances of a class like
# object
Dog = namedtuple("Dog", ["age", "breed", "name"])
sammy = Dog(age=5, breed="Husky", name="Sam")
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy.name)
print(sammy[0])

# Opening and Reading practice.txt and Folders
# Python OS Module
# command pwd will show current path
# Windows needs to have \\ in between locations
f = open("practice.txt", "w+")
f.write("This is a test string")
f.close()

# Show current directory
print(os.getcwd())

# List items in a directory
print(os.listdir())

# List all files and folders under a specific directory
print(os.listdir("C:\\Users"))

# Move practice.txt
# shutil.move(source, destination)
# shutil.move("practice.txt", "C:\\Users\\gistadr\\Documents\\PythonUdemyBootcamp\\AdvancedPythonModules\\Files")

# Delete a file
# There are 3 methods for deleting files:
# os.unlink(path) which deletes a file at the path you provide
# os.rmdir(path) which deletes a folder (folder must be empty) at the path you provide
# shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders
# contained in the path.
# All of these methods can not be reversed!
# Which means, if you make a mistake, you won't be able to
# recover the file.
# Instead, we will use the send2trash module.  A safer alternative
# that sends the deleted files to the trash bin instead.
send2trash.send2trash("practice.txt")

# os.walk
# Directory tree generator
# takes a parameter top
# yields a 3-tuple, directory path, directory names, and filenames
for folder, sub_folders, files in os.walk(os.getcwd()):
    print(f"Folder: {folder}\n Sub-folders: {sub_folders}\n Files: {files}")

# Python Datetime Module
# time(hour, min, second, microsecond, timezone info)
# If information is not provided it will automatically fill it in
# 20 minutes past 2 am (24 hour clock)
# Date is not associated with time
# my_time = datetime.time(13, 20, 1, 20)
# print(my_time)
# print(my_time.minute)
# print(my_time.hour)
# print(type(my_time))

# Date objects
# Get date information on today yyyy/mm/dd
# today = datetime.date.today()
# print(today)
# print(today.year)
# print(today.month)

# C time formatting
# today.ctime()
# print(today.ctime())

# Date and Time information
my_datetime = datetime(2021, 10, 3, 14, 20, 1)
print(my_datetime)

# Replace Datetime information
# Updating does not happen in place, must be assigned
my_datetime = my_datetime.replace(year=2020)
print(my_datetime)

# Perform arithmetic to solve for time difference
# Date
date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
time_delta = date1 - date2
print(time_delta)

# Datetime
datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)
# Returns total days and total hours/seconds
datetime_delta = datetime1 - datetime2
print(datetime_delta)
print(datetime_delta.seconds)

# Math and Random Modules
# help(math) to get help on function for math
value = 4.35
print(math.floor(value))  # rounds down to the nearest int
print(math.ceil(value))  # rounds up to the nearest int
print(round(value))   # True rounding

# Math Constants
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
# Numpy library, library specific for numerical processing

# Log-metric
print(math.log(math.e))
print(math.log(100, 10))

# Trigonometric
print(math.sin(10))
print(math.degrees(math.pi/2))
print(math.radians(180))

# Random
print(random.randint(0, 100))

# Seeded random number generator
random.seed(101)
print(random.randint(0, 100))

# Random item from list
my_list = list(range(0, 20))
print(random.choice(my_list))
# Sample with replacement (allowing the same element being chosen more than once)
print(random.choices(population=my_list, k=10))
# Sample without replacement (elements can only be picked once)
print(random.sample(population=my_list, k=10))
# Shuffle list (in place)
print(random.shuffle(my_list))
# Probability distribution
# randomly pick a value between a and b (floating point precision)
print(random.uniform(a=0, b=100))
# normal distribution
# gauss takes in a mean and a standard deviation
print(random.gauss(mu=0, sigma=1))

# Debugger
x = [1, 2, 3]
y = 2
z = 3

result_one = y + z

# Allows you to explore and call variables at a point in time
# pdb.set_trace() # hit 'q' to quit the debugger

# result_two = y + x

# Python Regular Expressions (regex)
# re library "import re"
# The re library allows us to create specialized pattern strings and then
# search for matches within text.
# The primary skill set for regex is understanding the special syntax for these
# pattern strings.
# Understand how to look up information for patterns
text = "The agent's phone number is 408-555-1234.  Call soon!"
pattern = "phone"
match = re.search(pattern, text)
print(match)
print(match.span())
print(match.start())
print(match.end())
print(match.group())

# Find multiple matches
matches = re.findall(pattern, text)
print(matches)
print(len(matches))

# Iterate through matches
for match in re.finditer(pattern, text):
    print(match)


# Regex Patterns
# "\d"  a digit ex) file_\d\d
# "\w"  Alphanumeric ex) \w-\w\w\w
# "\s"  White space ex) a\sb\sc
# "\D"  A non digit ex) \D\D\D
# "\W"  Non-alphanumeric ex) \W\W\W\W
# "\S"  Non-whitespace ex) \S\S\S\S
pattern = r"\d\d\d-\d\d\d-\d\d\d\d"
phone = re.search(pattern, text)
print(phone)
print(phone.group())

# More efficient pattern with quantifiers
# "+"  Occurs one or more times ex) Version \w-\w+
# "{3}"  Occurs exactly 3 times ex) \D{3}
# "{2,3}"  Occurs 2 to 4 times ex) \d{2,4}
# "{3,}"  Occurs 3 or more times ex) \w{3,}
# "*"  Occurs zero or more times ex) ABC*
# "?"  Once or none ex) plurals?
pattern = r"\d{3}-\d{3}-\d{4}"
phone = re.search(pattern, text)
print(phone)

# Compile function
# Compiles together different regular expression pattern codes
# The parentheses mean it is a group of a pattern
# You can call the groups individually
phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
results = re.search(phone_pattern, text)
print(results.group())  # Whole match, grouped together
print(results.group(1))  # index for group ordering starts at 1
print(results.group(3))

# Or operator
# if you use the "|" in a regex expression you can search for multiple
re.search(r"cat|dog", "The cat is here")

# Wildcard operator "."
re.findall(r".at", "The cat in the hat sat there")

# Starts with "^" and ends with "$"
re.findall(r"^\d", "1 is a number")
re.findall(r"\d$", "The number is 2")

# Exclude "[^]" - Grouping for Exclusion
# This is a common way of getting punctuation in a sentence
phrase = "There are 3 numbers 34 inside 5 this sentence"
pattern = r"[^\d]+"
print(re.findall(pattern, phrase))
test_phrase = "This is a string! But it has punctuation.  How can we remove it?"
this_is_clean = re.findall(r"[^!.? ]+", test_phrase)
" ".join(this_is_clean)

# Include "[] = Grouping for Inclusion
text = "Only find the hyphen-words in this sentence.  But you do not know how long-ish they are"
pattern = r"[\w]+-[\w]+"
print(re.findall(pattern, text))

# Multiple options for matching
text = "Hello, would you like some catfish?"
text_two = "Hello, would you like to take a catnap?"
text_three = "Hello, have you seen this caterpillar?"

re.search(r"cat(fish|nap|pillar)", text)


# Timing Your Code
# To find the most efficient approach, time code performance
# func_one making a list of strings up to a range of numbers
def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str, range(n)))


func_one(10)
func_two(10)


# You can check time before and after
# Current Time Before
start_time = time.time()
# Run Code
result = func_one(100000)
# Current Time After Running Code
end_time = time.time()
# Elapsed Time
elapsed_time = end_time - start_time
print(elapsed_time)

start_time = time.time()
# Run Code
result = func_two(100000)
# Current Time After Running Code
end_time = time.time()
# Elapsed Time
elapsed_time = end_time - start_time
print(elapsed_time)

# Timeit Module
run_times = 100000
stmt = """
func_one(100)
"""
setup = """
def func_one(n):
    return [str(num) for num in range(n)]
"""
print(timeit.timeit(stmt, setup, number=run_times))

stmt2 = """
func_two(100)
"""
setup2 = """
def func_two(n):
    return list(map(str, range(n)))
"""
print(timeit.timeit(stmt2, setup2, number=run_times))

# Zipping and Un-zipping files
f = open("file_one.txt", "w+")
f.write("One File")
f.close()
f = open("file_two.txt", "w+")
f.write("Two File")
f.close()
f = open("file_three.txt", "w+")
f.write("Three File")
f.close()

# Create Zipfile
comp_file = zipfile.ZipFile("comp_file.zip", "w")
# Compress and write passed in file to zip file
comp_file.write("file_one.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("file_two.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()  # Close when done zipping

# Extract zip file
zip_obj = zipfile.ZipFile("comp_file.zip", "r")
zip_obj.extractall("extracted_content")

# Use shell utility library to zip folders
dir_to_zip = "C:\\Users\\gistadr\\Documents\\PythonUdemyBootcamp\\AdvancedPythonModules\\AdvancedModules\\extracted_content"
output_filename = "example"
shutil.make_archive(output_filename, "zip", dir_to_zip)

# Extract with shutil
shutil.unpack_archive("example.zip", "final_unzip", "zip")
