#################################################
#                                               #
# Modules and Libraries                         #
#                                               #
#################################################

# Modules are pre-written libraries that can be imported for use in your code. They are usually put at the top of your code.
# There are three types of modules; the ones you've written yourself, third-party external sources and the preinstalled standard library.
# The standard library is ONE OF THE MAIN STRENGHTS with Python.
# Examples of most useful standard modules are: string, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse, sys.
# For a full list of all modules go to https://docs.python.org/3/py-modindex.html 
# Note how some modules are written in python and some are written in c. Some are only available to certain platforms, windows or linux
# There are two ways to import modules. You can either import the whole module by simply using the import function. 
import random

# For help on what's included in any module, you can print the help. Tip: You can print from the python console.. That's a bit easier than actually having it in your code.
# Syntax is: print(help('<module>'))
# I found the function getrandbits in the help as per below and wanted to use it.
# getrandbits(...)
#    getrandbits(k) -> x.  Generates an int with k random bits.

# After full import can now use any function the module. In our case "random". We call our getrandbits function.
# You call the functions in the module by <module>.<function>
print("this is a random number from 8 bits:", random.getrandbits(8))

# If we want to selectively import just specific variables/objects/functions rather than a whole module, we can do so by using from <module> import <object>
# In this example we import the constant pi from the math module
from math import pi
print("pi from our math module is:", pi)

# We can also import modules and or their objects and rename them to make names more explanatory to our liking by using from <module> import <object> as <name>
# Or in the module case import <module> as <name>
from math import sqrt as square_root
print ("Square root of 100 is:", square_root(100))

# Importing today's date from datetime and printing it. 
from datetime import date, datetime
print("Today's date is:", date.today())
print("Today is as per unix weekday number: ", datetime.weekday(date.today()))

# Third Party modules are commonly installed via PyPI, Python Package Index.
# The best way to install these packages are through an application called pip.
# pip comes with most installation of python and is run in the command line.
# pip install <library_name>
# You can micro manage versions of modules and create virtual environments to store them in. pip grows quite comprehensive and complex.

#################################################
#                                               #
# Functions                                     #
#                                               #
#################################################

#We've used functions in the previous lessons. These are examples of functions:
print("Hello World")
range(2, 20)
str(12)
range(10,20,3)
#The values inside the parenthesis are called function arguements

#We can define our own functions and later call them in our code.
def my_function():
    print("Hello World")
#calling our function by typing it followed by parenthesis
my_function()

# You can also define functions with parameters that take arguments as input
# Note how the parameters can't be used outside the function, they are local to the function!
def my_function2(argumentx):
    print(str(argumentx) + "!")
# We call the function and give it an argument
my_function2("spam")
my_function2(2)

# This can of course be made to have multiple arugements
def my_function3(argumenty, argumentz):
    print(argumenty + " something " + argumentz)
my_function3("before","after")

# You can also return values from functions such as ints and strings
# We convert the arguments to strings to be able to do our concatenation
def my_function4(string1, string2):
    concatenated_strings = str(string1) + str(string2)
    return(concatenated_strings)
# Note how you have to save the return value in a value (I think this is mandatory at least!)
combined = my_function4(1, "these")
print (combined)

# Syntax for return seem to be able to be return() or just return <value>
# Note how using return immediately exits the function, and stops the processing of the rest of the function!
def shortest_string(string1, string2):
    if len(string1) == len(string2):
        return "your strings are of equal length"
    elif len(string1) < len(string2):
        return string1
    else:
        return string2
    print("This will never be printer, ever")

# Let's compare our strings. I haven't found a way to print a returned string straight away without first storing it in a variable.
shortest_string = shortest_string("hello", "worlds")
print(shortest_string)

# Another function example to multiply arguments and return the sum
def multiply_arguments(x,y):
    sum = x * y
    return sum

# Call the function and printing the result straight away works fine
print(multiply_arguments(5, 12.0))

# Comments in python are started with # symbols.
# There is also something called docstrings that are comments preserved through runtime.
# This means that you will be able to see explanatory comments during the runtime of your code
# They are defined with triple quotation marks at the start an end of the docstring
def shout():
    """
    Below code will print Some string
    """ 
    print("Some string") 

# You can even access the docstrings if you want and print them! You do so by using double underscore, doc and the double underscore again.
# In this example we refer to a specific function's docstring by calling it like this:
print(shout.__doc__)