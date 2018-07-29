#################################################
#                                               #
# Pythonicness & Packaging                      #
#                                               #
#################################################

# Writing programs that actually do what they're supposed to do is just one componetn of being a good python programmer
# It's important to write clean code that is easily understood, even weeks after you programmed it.
# One way of practicing this is to follow the "Zen of Python".

import this

##################################################
# Python Enhanced Proposals (PEP)                #
##################################################

# Python Enhanced Proposals (PEP) are suggestions for improvements to the language, made by experienced Python developers.

# PEP 8 is a style guide of making code readable. Summary of guidelines are:

# Modules should have short, all lowercase names
# Class names should be in CapWords style
# most variable and function names should be lowercase_with_underscores
# constant (variables that never change) should be CAPS_WITH_UNDERSCORES
# names that would class with Python keywords such as class of if should have trailing underscores
# Use whitespaces around operators to increase readability, but don't overdo whitespace, avoid it inside any type of brackets.
# Lines shouldn't be longer than 80 characters
# From module import * should be avoided
# There should be only one statement per line
# Use spaces rather than tabs to indent, but doesn't really matter, stick to one of them.

# PEP 257 - style conventions for dosctrings, PEP 20 - the Zen of Python

##################################################
# Function Arguments                             #
##################################################

# Python allows for functions with VARYING number of arguments. This is done by using *args as a function parameter.
# The arguments are accessible as the tuple() args.
# *args is just a convention, you can you any name you choose here. The varying number of argument must naturally come AFTER named arguments.

def function(named_arg, *args):
    print(named_arg)
    print(args)

function(5, 5, 8, "hello")

# Named arguments for functions can also be assigned default values, if we wish.
# If arguments are passed to the function the default values are overridden.
# The default arguments must be put after named arguments to have an effect, naturally.
# But can of course be followed by *args or **kwargs that can take any number of arguments.

def function2(x, y, food = "spam"):
    print("x is:", x)
    print("y is:", y)
    print("food is:", food)

function2(1, 2)
function2(1,2,"egg")

# Keyword Arguments, or **kwargs, allows us to handle named arguments that have not been defined in advance.
# The keyword arguments return a dictionary in which the keys are the argument names, and the values the argument values.

def function3(x, y=7, *args, **kwargs):
    print("x is:", x)
    print("y is:", y)
    print("args is:", args)
    print("keyword args is:", kwargs)

function3(2, 3, 4, 5, 6, a=7, b=8)

##################################################
# Tuple Unpacking                                #
##################################################

# Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.
numbers = (1, 2, 3)
a, b, c = numbers
print(a,b,c)

# This can also be used to swap variables. This is a python specific feature, in most other languages you would have to use auxiliary variables to do this.
a,b = b,a
print (a,b,c)

# You can create a catch-all-remaining variable for the leftover values in the unpacking.
# This is done by a pre-facing * of the variable. 
numbers = (1,2,3,4,5,6,7,8,9)
a, b, *c, d = numbers
print("a = {}, b = {}, c = {}, d = {} ".format(a,b,c,d))

###################################################
# Ternary Operator / conditional quick expression #
###################################################

# Ternary operator is a method of simplifying a conditional expression.
# These shouldn't be overused as they may reduce readability, but they do lessen the amount of code needed.
# Apparently it's good when assigning variables, sometimes.

a = 7
b = 1 if a >= 5 else 42
print ("b was assigned 1 as the if statement was fulfilled. Value of b is: ", b)

##################################################
# Else                                           #
##################################################

# Else statements are most commonly used along with the if() statement. However, it can also be used with for() and while()
# If you use else in conjunction with for or while, the meaning of it changes.
# Else in these cases means that the code within it is run if the previous loop was finished normally

for i in range (10):
    if i == 100:
        break
else: 
    print ("Previous loop finished without break") 

for i in range (10):
    if i == 9:
        print("For loop matched its condition, breaking out of the loop")
        break
else: 
    print ("Previous loop finished without break") 

# else can also be used with try/except statements. In this case, the code within it is only executed if no error occurs in the try statement

try:
    print(1)
except(TypeError):
    print(2)
else:
    print(3)

try:
    print(1 + "1" == 2)
except(TypeError):
    print(2)
else:
    print(3)

##################################################
# More on __main__                               #
##################################################

# Most python code is aimed to be either a module (which is later imported) or a script that is run by itself.
# You can by special code, allow for both usecases (both being imported as a module, or run as a script) to be written in the same file.
# To achieve this, the code block if __name__ == "__main__" is used to ensure that what directly follows this line will be executed
# at RUNTIME in a script, but never executed during IMPORT as a MODULE.

def module_function():
    print("This is a module function")

if __name__ == "__main__":
    print("This is a script")

# To prove the point we have broken out the above code into a "module" called sololearn.py.
# We import that as a module and run the module function called module_function().
import sololearn as sololearn
sololearn.module_function()

##################################################
# Major 3rd Party Libraries                      #
##################################################

# The Python standard library alone contains extensive functionality.
# However, some tasks require 3rd party libraries. Some major 3rd party libraries are:
# Django - The most frequently used web framework written in Python. Django powers websites that include instragram and Disqus. Heaps of functionality and extension packs.

# CherryPy and Flask are also very popular web frameworks.
# For scraping data from websites, the library BeautifulSoup is very useful, and leads to better results than building your own scraper with regular expressions.

# matplotlib allows you to create graphs based on data in python.
# NumPynallows for use of multidimensional arrays that are much faster than native python solution of nested lists

