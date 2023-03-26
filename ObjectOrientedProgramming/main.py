# Object-Oriented Programming
# Attributes and Class Keyword
# User defined object - blueprint that defines the nature of a future object
# Class names should be capitalized and camel case
import math

class Dog:
    # Class Object Attribute (same for any instance of a class)
    species = "mammal"

    # Constructor used to create the instance/attributes of the class
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    # Class Methods (Operations/Actions)
    # A Method is a Function that is inside a class
    def bark(self):
        print(f"{self.name} says: WOOF!")


# Defined instance of Dog class
my_dog = Dog("Husky", "Bruno", False)
print(f"Breed: {my_dog.breed}, Name: {my_dog.name}, Has Spots: {my_dog.spots}, Species: {my_dog.species}")
print(type(my_dog))
my_dog.bark()


class Circle:
    # Class Object Attribute
    pi = 3.14

    # Initialization/Construction
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi  # or if class obj attribute Circle.pi instead of self.pi

    # Methods
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)
print(my_circle.get_circumference())
print(my_circle.area)


# Inheritance and Polymorphism
# Form new classes using classes that are already defined (reduce complexity)
class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()


# Inheritance - Derived Class
class Dog2(Animal):
    def __init__(self):
        # Creates an instance of the animal class when Dog2 is created
        Animal.__init__(self)
        print("Dog Created")

    # Overwrite Method
    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("WOOF!")

    def eat(self):
        print("I am a dog and am eating")


my_dog = Dog2()
my_dog.eat()
my_dog.who_am_i()


# Polymorphism
class Dog3:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog3("Niko")
felix = Cat("Felix")
print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())


def pet_speak(pet_critter):
    print(pet_critter.speak())


pet_speak(niko)
pet_speak(felix)


# Abstract Class
# Serves only as a base class
class Creature:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


my_creature = Creature("Fred")
# my_creature.speak()  # Error not supposed to use abstract class


# Implement Abstract class
class Dog4(Creature):
    def speak(self):
        return self.name + " says woof!"


class Cat2(Creature):
    def speak(self):
        return self.name + " says meow!"


fido = Dog4("Fido")
isis = Cat2("Isis")
print(fido.speak())
print(isis.speak())


# Special (Magic/Dunder) Methods
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


b = Book("Python rocks", "Jose", 200)
print(b)
del b  # delete variable


# Homework
# Fill in the Line class methods to accept coordinates as a pair of tuples
# and return the slow and distance of the line
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.dist(self.coor1, self.coor2)

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


# Fill in the class
class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * math.pi * self.radius ** 2

    def surface_area(self):
        return (2 * (math.pi * self.radius ** 2)) + (2 * math.pi * self.radius * self.height)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())


# Object-Oriented Programming - Challenge
# Create a bank account class that has two attributes: owner, balance
# and two methods: deposit, withdraw
# As an added requirement, withdrawals, may not exceed available balance
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(f"Account for {self.owner} has deposited ${amount}, Total Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Unable to make withdrawal of ${amount}, Remaining balance is ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful, Total Balance: ${self.balance}")


acct1 = Account("Jose", 100)
print(acct1)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
