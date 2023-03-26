# Object and Data Structure Basics
# Python uses Dynamic Typing where C++ is Statically Typed
# You can use the type() function in Python to check the data type
# of variables

# int - whole numbers
# float - numbers with decimal point
# str - strings, words, etc
# list - ordered sequence of objects [10, "hello", 200.3]
# dict - unordered key:value pairs {"myKey":"value", "name":"Frankie"}
# tup - ordered immutable sequence of objects (10, "hello", 200.3)
# set - unordered collection of unique objects {"a", "b"}
# bool - logical value indicated true or false

# Variable Assignments
a = 10
b = a + a
print(type(a))
a = 3.5
print(type(a))

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)

# Strings
print('hello')
print("world")
print('this is also a string')
print(" I'm going on a run ")
# Escape sequences
print("hellow \nworld")  # \n new line
print("hellow \tworld")  # \t tab
# len() length of string
len("hello")
len("I am hungry")

# Indexing and Slicing with Strings
myString = "Hello World"
# Indexing
print(myString[0])
print(myString[8])
print(myString[-2])  # backwards, negative index position
myString = "abcdefghijk"
# Slicing
print(myString[2:])
print(myString[:3])  # got up to index 3 but do not include it
print(myString[3:6])
print(myString[1:3])
# Step Size
print(myString[::])  # all the way from the beginning to all the way at the end
print(myString[::2])  # jumping in step size of 2
print(myString[2:7:2])
print(myString[::-1])  # Reverse string

# String Properties and Methods
# Immutability - Cannot mutate, cannot change
name = "Sam"
last_letters = name[1:]
# Concatenation
pam = 'P' + last_letters
print(pam)
x = "Hello World"
x += " it is beautiful outside!"
print(x)
letter = 'z'
letter *= 10
print(letter)
# Methods
x = "Hello World"
x.upper()  # uppercase everything in the string
x.lower()  # lowercase everything in the string
x.split()  # split a string based on white space or letter you pass in

# Print Formatting with Strings
# .format() method
print("This is a string {}".format("Inserted"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
# float formatting "value:width.precision f}"
result = 100/777
print("The result was {r:1.3f}".format(r=result))
# f strings - formatted string literals
name = "Jose"
print(f"Hello, his name is {name}")
name = "Sam"
age = 3
print(f"{name} is {age} years old.")

# Lists in Python
my_list = [1, 2, 3]
print(len(my_list))
my_list = ["one", "two", "three"]
print(my_list[0])
print(my_list[1:])
another_list = ["four", "five"]
my_list += another_list
print(my_list)
my_list[0] = "ONE ALL CAPS"
print(my_list)
my_list.append("six")  # add item to end of list
print(my_list)
popped_item = my_list.pop()  # removes an item from the end of the list, will return the removed element
print(my_list)
print(popped_item)
my_list.pop(0)  # removes element at the supplied index
print(my_list)
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
new_list.sort()
num_list.sort()
print(new_list)
print(num_list)
num_list.reverse()
print(num_list)
# Another way to sort returns the list itself
sorted(num_list)

# Dictionaries in Python
# Unordered mapping (key/value) pair
# {'key1':'value1', 'key2':'value2'}
# Cannot be sorted
my_dict = {'key1': "value1", 'key2': "value2"}
print(my_dict)
print(my_dict['key1'])
prices_lookup = {"apple": 2.99, "oranges": 1.99, "milk": 5.80}
print(prices_lookup["apple"])
d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insideKey": 100}}
print(d["k2"])
print(d["k3"]["insideKey"])
d = {"k1": 100, "k2": 200}
d["k3"] = 300
print(d)
d["k1"] = "New Value"
print(d)
print(d.keys())
print(d.values())
print(d.items())

# Tuples in Python
# immutable
t = (1, 2, 3)
mylist = [1, 2, 3]
print(type(t))
print(type(mylist))
print(len(t))
t = ("one", 2)
print(t[0])
t = ("a", "a", "b")
print(t.count("a"))  # returns how many times that element appears
print(t.index("a"))  # returns the index of the first element occurrence
mylist[0] = "NEW"

# Sets in Python
# unordered collections of unique elements
my_set = set()
my_set.add(1)
my_set.add(2)
print(my_set)
my_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]
set(my_list)

# Booleans in Python
# True / False must be capitalized
test = 1 > 2
b = None  # placeholder data

# I/O Basics Files in Python
my_file = open("test.txt")
print(my_file.read())  # returns a string of everything in the text file
my_file.seek(0)  # resets the cursor to 0 so you can read again
contents = my_file.read()
my_file.seek(0)
contents02 = my_file.readlines()
my_file.close()  # must close file after use

# New way of opening file
with open("test.txt") as my_new_file:
    my_contents = my_new_file.read()
    # Will automatically close file

# File locations
# In windows to change file locations you need to use double \\
# ex) "C:\\Users\\UserName\\Folder\\test.txt"
with open("test.txt", mode="r") as my_file:
    my_contents2 = my_file.read()
with open("test.txt", mode="a") as my_file:
    my_file.write("\nFour on Fourth")
with open("test2.txt", mode="w") as my_file:
    my_file.write("I created this file!")
with open("test2.txt", mode="r") as my_file:
    print(my_file.read())

# Python Comparison Operators
print(2 == 2)
print(2 == 1)
print("hello" == "bye")
print("2" == 2)
print(2.0 == 2)
print(3 != 3)
print(2 > 1)
print(1 > 2)
print(1 < 2)
print(2 >= 2)
print(4 <= 1)

# Python Logical Operators
print(1 < 2 & 2 < 3)
print(1 < 2 and 2 < 3)
print(1 < 2 | 2 < 3)
print(1 < 2 or 2 < 3)
print(1 < 2 > 3)  # chaining
print(not(1 == 1))
