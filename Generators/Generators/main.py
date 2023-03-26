# Generators
# Generator functions allow us to write a function that
# can send back a value and then later resume to pick up
# where it left off
# This type of function is a generator in Python, allowing
# us to generate a sequence of values over time.
# The main difference in syntax will be the use of a
# yield statement.
# When a generator function is compiled they become an
# object that supports an iteration protocol.
# That means when they are called in your code they don't
# actually return a value and then exit.
# Generator functions will automatically suspend and resume
# their execution and state around the last point of value
# generation.
# The advantage is that instead of having to compute an
# entire series of values up front, the generator
# computes one value waits until the next value is called for
import random

# More efficient way of getting values
# Generating values as you need them
def create_cubes(n):
    for x in range(n):
        yield x**3


# You need to iterate through the generator if you want
# the values
# It can be cast to a list
for x in create_cubes(10):
    print(x)


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        # a will = b, and then b will = a + b
        a, b = b, a + b


for number in gen_fibon(10):
    print(number)


# Next Function
def simple_generator():
    for x in range(3):
        yield x


# Generator object
g = simple_generator()
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
# print(next(g))  # No longer has any next

# Iter function
# Convert objects that are iterable into iterators
s = "hello"
s_iter = iter(s)
next(s_iter)


# Create a generator that generates the squares of numbers up to some number
def square_gen(n):
    for num in range(n):
        yield num ** 2


for num in square_gen(50):
    print(num)


# Create a generator that yields "n" random numbers between
# low and high number that are inputs
def rand_generator(low, high, n):
    for num in range(n):
        yield random.randint(low, high)


for num in rand_generator(5, 100, 25):
    print(num)

# generator comprehension
# It turns a list comprehension into a generator comprehension
my_list = [1, 2, 3, 4, 5]
gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item)
