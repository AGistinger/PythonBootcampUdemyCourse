# Errors and Exceptions Handling
def add(n1, n2):
    print(n1 + n2)


add(10, 20)
number1 = 10
number2 = int(input("Please provide a number: "))
add(number1, number2)

print("Something happened!")

# Try / Except / Else
try:
    # Want to attempt this code, may have an error
    result = 10 + 10
except:
    # What you want to happen if there is an error
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)

# Try / Except / Finally
try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error!")
finally:
    # always going to execute
    print("I always run")


# Function try/catch/finally
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print(f"Yes, thank you for number {result}")
            break
        finally:
            print("End of try/except/finally")


ask_for_int()

# Errors and Exceptions Homework
# Problem 1 - Handle the exception thrown by the code below
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print(f"'{i}' is not a number and cannot go to the power of 2")


# Problem 2 - Handle the exception thrown by the code below
try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print(f"You cannot divide {x} by {y}, Divide by Zero Error")
finally:
    print("All Done")


# Problem 3 - Write a function that asks for an int and prints the square of it
# User a while loop with a try, except and else block to account for incorrect input
def ask_input():
    user_result = ""
    while not type(user_result) == int:
        try:
            user_result = int(input("Please enter a integer number: "))
        except ValueError:
            print(f"{user_result} is not a valid integer")
        else:
            print(user_result ** 2)


ask_input()

# Running tests with Unittest Library
