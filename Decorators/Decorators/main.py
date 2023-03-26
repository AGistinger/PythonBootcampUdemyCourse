# Decorator
# Decorators allow you to "decorate" a function
# Python has decorators that allow you to tack on
# extra functionality to an already existing function.
# They use the @ operator and then are placed on top
# of the original function.

# Passing functions to other functions
def func():
    return 1


def hello(name="Jose"):
    print("The hello() function has been executed")

    def greet():
        return "\t This is the greet function inside hello"

    def welcome():
        return "\t This is welcome() inside hello"

    print("I am going to return a function!")

    if name == "Jose":
        return greet
    else:
        return welcome


func()
hello()
my_new_func = hello("Jose")
print(my_new_func())


def cool():
    def super_cool():
        return "I am very cool!"

    return super_cool


some_func = cool()
print(some_func())


def hello2():
    return "Hi Jose"


def other(some_def_func):
    print("Other code runs here")
    print(some_def_func())


other(hello2)


# Decorator
def new_decorator(original_func):

    def wrap_func():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code after the original function")

    return wrap_func


# Will call the wrapper for "new_decorator"
@new_decorator
def func_needs_decorator():
    print("I want to be decorated")


decorated_func = new_decorator(func_needs_decorator)
decorated_func()
func_needs_decorator()
