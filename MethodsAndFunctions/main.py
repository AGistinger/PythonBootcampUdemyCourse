# Methods and Functions
from random import shuffle
from math import pi
import string

# Methods
my_list = [1, 2, 3]
my_list.append(4)
my_list.pop()
print(my_list)
my_list.insert(0, 5)
print(my_list)


# Functions
def say_hello(name="Default"):
    print(f"Hello {name}!")


say_hello("Jose")
say_hello()


def add_num(num1, num2):
    if (type(num1) != int) or (type(num2) != int):
        print("Invalid type of argument, please use integers")
    else:
        return num1 + num2


print(add_num(10, 20))
add_num("5", "X")


# Logic with Python Functions
# Return True if any number is even inside a list
def is_even(num_list):
    for number in num_list:
        if type(number) == int:
            if number % 2 == 0:
                return True
        else:
            return number + " is not an int"
    return False


print(is_even([1, 3, 5]))
print(is_even([1, 7, 10]))
print(is_even(["Fifty", "Zero", "Alex"]))


# Return all even numbers in a list
def is_even_list(num_list):
    even_list = []
    for number in num_list:
        if type(number) == int:
            if number % 2 == 0:
                even_list.append(number)
        else:
            return number + " is not an int"
    return even_list


# Functions and Tuple Unpacking
stock_prices = [("APPL", 200), ("GOOG", 400), ("MSFT", 100)]
work_hours = [("Abby", 100), ("Billy", 400), ("Cassie", 800)]


def employee_check(employee_hours):
    current_max = 0
    employee_of_month = ""

    for name, hours in employee_hours:
        if (type(name) == str) and (type(hours) == int):
            if hours > current_max:
                employee_of_month = name
                current_max = hours
        else:
            print(f"The tuple of {name} and {hours} are the incorrect types")
            return

    return employee_of_month, current_max


print(employee_check(work_hours))

# Interactions between Python Functions
example = [1, 2, 3, 4, 5, 6, 7]
shuffle(example)  # Does not return the list
print(example)


# Three Card Monte Game
def shuffle_list(item_list):
    shuffle(item_list)
    return item_list


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2 ")
    return int(guess)


def check_guess(card_list, guess):
    if card_list[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(card_list)


card_monte = [' ', 'O', ' ']
shuffled_list = shuffle_list(card_monte)
my_guess = player_guess()
check_guess(shuffled_list, my_guess)


# *args and **kwargs in Python (functional parameters)
# arguments and keyword arguments
# allows you to pass in many parameters as a tuple
def myfunc(*args):
    # returns5% of the sum of a and b
    return sum(args) * 0.05


myfunc(40, 60)


# dictionary key/value pairs multiple arguments
def my_func(**kwargs):
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")


my_func(fruit='apple', veggie='lettuce')


def my_func_a(*args, **kwargs):
    print("I would like {} {}".format(args[0], kwargs['food']))


my_func_a(10, 20, 30, fruit='orange', food='eggs', animal='dog')


def my_func_b(string):
    mod_string = ""
    for letter in string:
        if string.index(letter) % 2 == 0:
            mod_string = mod_string + letter.upper()
        else:
            mod_string = mod_string + letter.lower()
    return mod_string


print(my_func_b("gryphoncat"))


# FUNCTION PRACTICE EXERCISES
# Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both
# numbers are odd
def lesser_of_two_evens(a, b):
    if (a % 2 == 0) and (b % 2 == 0):
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))


# Write a function that takes a two-word string and returns True if
# both words begin with the same letter
def animal_crackers(text):
    strings = text.split()
    if strings[0][0] == strings[1][0]:
        return True
    else:
        return False


print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Kangaroo"))


# Given two integers, return True if the sum of the integers is 20 or
# if one of the integers is 20.  If not, return False
def makes_twenty(n1, n2):
    if(n1 == 20) or (n2 == 20):
        return True
    elif n1 + n2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))
print(makes_twenty(2, 3))
print(makes_twenty(15, 5))


# Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    mod_string = ""
    for index, letter in enumerate(name):
        if(index == 0) or (index == 3):
            mod_string += letter.upper()
        else:
            mod_string += letter
    return mod_string


print(old_macdonald("macdonald"))


# Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    words = text.split()
    words.reverse()
    mod_text = " ".join(words)

    return mod_text


print(master_yoda("I am home"))
print(master_yoda("We are ready"))


# Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    if (abs(n - 100) <= 10) or (abs(n - 200) <= 10):
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def has_33(nums):
    prev_num = 0
    for num in nums:
        if (prev_num == 3) and (num == 3):
            return True
        prev_num = num
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


# Given a string, return a string where for every character in the original
# there are three characters
def paper_doll(text):
    mod_text = ""
    for letter in text:
        mod_text += (letter * 3)
    return mod_text


print(paper_doll("Hello"))
print(paper_doll("Mississippi"))


# Given three integers between 1 and 11, if their sum is less than
# or equal to 21, return their sum.  If their sum exceeds 21 and
# there's an eleven, reduce the total sum by 10.  Finally, if
# the sum (even after adjustment) exceeds 21 return "BUST"
def blackjack(n1, n2, n3):
    cards = [n1, n2, n3]
    total = sum(cards)
    if total <= 21:
        return total
    elif (total > 21) and (contains_11(cards)):
        total -= 10
        if total <= 21:
            return total
        else:
            return "BUST"
    else:
        return "BUST"


def contains_11(nums):
    for num in nums:
        if num == 11:
            return True
    return False


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


# Return the sum of the numbers in the array, except ignore sections
# of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9.  Return 0 for no numbers
def summer_69(arr):
    total = 0
    skip = False
    for num in arr:
        if num == 6:
            skip = True
            continue
        if num == 9:
            skip = False
            continue
        if not skip:
            total += num
    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


# Write a function that takes in a list of integers and returns True
# if it contains 007 in order
def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


# Write a function that returns the number of prime numbers that exist up
# to and including a given number
def count_primes(num):

    # Check for 0 or 1 input
    if num < 2:
        return 0
    ###############
    # 2 or greater
    ###############

    # Store our prime numbers
    primes = [2]
    # Counter going up to the input num
    x = 3

    # x is going through every number up to the input num
    while x <= num:
        # Check if x is prime
        for y in primes:
            if x % y == 0:
                x += 2
                break

        else:
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)


print(count_primes(100))


# Lambda Expressions, Map, and Filter Functions
# Map Function
def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

# Apply a function to every number in a list (Map function)
# Map function takes in a function and a container and applies
# That function to every element in the container
# map(function, container) <- syntax
for item in map(square, my_nums):
    print(item)

sq_nums = list(map(square, my_nums))


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return "EVEN"
    else:
        return my_string[0]


names = ["Andy", "Eve", "Sally"]
names_list = list(map(splicer, names))
print(names_list)


# Filter Functions
# Need to filter by a function that returns True or False
def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]
for n in filter(check_even, my_nums):
    print(n)

even_nums = filter(check_even, my_nums)
print(even_nums)


# Lambda expressions
# Syntax: lambda variable: return result
# def square(num):
#    result = num ** 2
#    return result
# square(3)

print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda num: num % 2 == 2, my_nums)))
print(list(map(lambda name: name[0], names)))

# Nested Statements and Scope
# L: Local - names assigned in any way within a function (def or lambda),
# and not declared in that function.
# E: Enclosing function locals - Names in the local scope of any and all
# enclosing functions (def or lambda), from inner to outer.
# G: Global (module) - Names assigned at the top-level of a module file,
# or declared global in a def within the file.
# B: Build-in (Python) - Names preassigned in the built-in names module:
# open, range, SyntaxError,...
x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())


def func():
    # Get global variable and change global variable
    global x
    print(f"X is {x}")
    x = "New Value"
    print(f"I just locally changed global X to {x}")


func()


# Methods and Functions Overview
# The volume of a sphere given as
def vol(rad):
    return (4 / 3) * pi * (rad ** 3)


print(vol(2))


# Write a function that checks whether a number is in a given range
def ran_check(num, low, high):
    return num in range(low, high + 1)


print(ran_check(5, 2, 7))


# Write a function that accepts a string and calculates the number of
# upper case letters and lower case letters
def up_low(s):
    d = {"upper": 0, "lower": 0}

    for char in s:
        if char.isupper():
            d["upper"] += 1
        elif char.islower():
            d["lower"] += 1
        else:
            continue

        print(f"Original String: {s}")
        print(f"Lowercase count: {d['lower']}")
        print(f"Uppercase count: {d['upper']}")


up_low("Hello Mr. Rogers, how are you this find Tuesday?")


# Write a function that takes a list and returns a new list with unique
# elements of the first list
def unique_list(lst):
    return list(set(lst))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# Write a function to multiply all the numbers in a list
def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print(multiply([1, 2, 3, -4]))


# Write a function that checks whether a word or phrase is a palindrome
def palindrome(s):
    # Remove spaces
    s = s.replace(" ", "")

    # Check if string == reversed string
    return s == s[::-1]


print(palindrome("nurses run"))


# Write a function to check whether a string is a pangram or not
def is_pangram(str1, alphabet=string.ascii_lowercase):
    # Create a set of the alphabet
    alpha_set = set(alphabet)
    # Remove any spaces from input string
    str1 = str1.replace(" ", "")
    # Convert the input string into all lowercase
    str1 = str1.lower()
    # Grab all unique letters from the string
    str1 = set(str1)
    # alphabet set == string set input
    return str1 == alpha_set


print(is_pangram("The quick brown fox jumps over the lazy dog"))
