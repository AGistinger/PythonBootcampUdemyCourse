# Python Statements / Control Flow

# import functions from library
from random import shuffle
from random import randint

# If Statements
hungry = True
if hungry:
    print("Feed Me!")
else:
    print("I'm not hungry")

loc = "Bank"
if loc == "Auto Shop":
    print("Cars are cool!")
elif loc == "Bank":
    print("Money is cool!")
elif loc == "Store":
    print("Welcome to the store!")
else:
    print("I do not know much.")

name = "Sammy"
if name == "Frankie":
    print("Hello Frankie!")
elif name == "Sammy":
    print("Hello Sammy")
else:
    print("What is your name?")

# For Loops in Python
# For variable in container:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_list:
    print(num)

# Looping with control flow
for num in my_list:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number: {num}")

list_sum = 0
for num in my_list:
    list_sum += num
print(list_sum)

my_string = "Hello World"
for letter in my_string:
    print(letter)

tup = (1, 2, 3)
for item in tup:
    print(item)

# Tuples in for loops
# Tuple unpacking, get the individual items in the tuple
my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
for (a, b) in my_list:
    print(a)
    print(b)

my_list = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]
for a, b, c in my_list:
    print(b)

# Iterate through a Dictionary
# You can do similar to tuples and define the key, value
# in the for loop definition and specify .items() to get
# the items from the dictionary key/value pair
# You can also use .values() to get values only from dictionaries
d = {"k1": 1, "k2": 2, "k3": 3}
for key, value in d.items():
    print(value)

# While Loops
# break: breaks out of the current closest enclosing loop
# continue: goes to the top of the closet enclosing loop
# pass: does nothing at all
x = 0
while x < 5:
    print(f"The current value of x is: {x}")
    x += 1
else:
    print("X is not less than 5")

# Pass
x = [1, 2, 3]
for item in x:
    pass  # Placeholder to avoid syntax error

# Continue
my_string = "Sammy"
for letter in my_string:
    if letter == "a":
        continue  # tells program to go back to top of loop
    print(letter)

# Break
for letter in my_string:
    if letter == "a":
        break  # stops loop

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

# Useful Operators in Python
# Range - Will generate the numbers up to but not including the number passed in
my_list = [1, 2, 3]
for num in range(10):
    print(num)

# Range - range(start, stop, stepSize)
for num in range(3, 10, 2):
    print(num)

list(range(0, 11, 2))  # get back the list of numbers

# Enumerate
# enumerate(container) - will return tuples containing the element and the index
word = "abcde"
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")

# Zip function (opposite of enumerate)
# returns tuples
# zip can only zip to the list that is the shortest
# everything else that is extra will be ignored
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']
my_list3 = [100, 200, 300]
for item in zip(my_list1, my_list2, my_list3):
    print(item)

# Put lists together
combined_list = list(zip(my_list1, my_list2, my_list3))

# In operator
test1 = 'x' in [1, 2, 3]
test2 = 'x' in ['x', 'y', 'z']
test3 = 'a' in "a world"
test4 = 'my_key' in {'my_key': 345}
d = {"my_key": 345}
test5 = 345 in d.values()
print(test1, test2, test3, test4, test5)

# Min/Max
my_list = [10, 20, 30, 40, 100]
print(min(my_list))
print(max(my_list))

# Shuffle function
# Does not return list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(my_list)
print(my_list)

# Random int function
# randint(lowerRange, upperRange)
# Returns an int
print(randint(0, 100))

# Accept User Input
result = int(input("Enter a number here: "))
print(f"You entered: {result}")
print(type(result))

# List Comprehensions in Python
# Flattened out for loop
my_string = "hello"
my_list = [letter for letter in my_string]

# element for element in container
my_list = [x for x in "word"]
print(my_list)

my_list = [num**2 for num in range(0, 11)]
my_list = [x for x in range(0, 11) if x % 2 == 0]

celcius = [0, 10, 20, 34.5]
fahrenheit = [(9/5 * temp + 32) for temp in celcius]
print(fahrenheit)

# not good coding for list comprehension hard to read
results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]

my_list = []
for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        my_list.append(x * y)

# List comprehension
my_list = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(my_list)

# Write a program that prints the integers from 1 - 100
# but in multiples of 3 print fizz and mutliples of 5 print buzz
# for multiples of both 3 and 5 print FizzBuzz
for num in range(0, 101):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
