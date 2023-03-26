# one.py
# When you call a python script:
# All the code at indentation level 0 will be run
# There is no main() function like other languages (C++, Java)
# There is a built-in variable called __name__
# import myModule

# print("hello")
def func():
    print("FUNC() IN ONE.PY")


print("TOP LEVEL IN ONE.PY")

# Assign string to the __name__ variable
# Organize code on what you want to execute
if __name__ == "__main__":
    # RUN THE SCRIPT
    # myModule.my_func()
    print("ONE.PY IS BEING RUN DIRECTLY")
    # LOGIC EXECUTE FUNCTIONS
    func()
else:
    print("ONE.PY has been imported")
