#################################################
#                                               #
# Functional Programming                        #
#                                               #
#################################################

# Functional programming is focused around functions, just like the name suggests.
# A key part of it is higher-order functions. Higher-order functions take other functions as arguments, or return them as results.

# Simple example of how a higher-order function can be used:
# This function takes a function and an argument as arguments. It runs the function with its argument once and then uses the return value as an argument to run it again.
def apply_twice(func, arg):
    return func(func(arg))

# This function simply adds the value 5 to the input and return the sum.
def add_five(x):
    return x + 5

# Calling the function apply_twice with arguments of function add_five and the integer 10.
print (apply_twice(add_five, 10))

#########################
# Pure Functions        #
#########################

# Functional programming seeks to use pure functions.
# Pure functions are functions that have no side effects.
# They also return a value that depends ONLY on their arguments.
# They can be run any amount of time and have the same output every time.

# Pure functions are considered easier to reason about and test. They are more efficient as you can store the result of the function in a variable so that can be referred 
# the next next itme the function of that input is needed. This reduces the number of times you need to call the function. This is called MEMOIZATION. The impure functions are 
# easier to run in parallel.

# So what about disadvantages?
# Well, the impure functions are more difficult to write in certain situations. Also i/o is supposedly harder, as i/o inherently require side effects.

# The best example I can find between a pure function and an impure function is:

# Pure function
def f(x):
    return x + 1

# Impure function, commenting out the function isTuesday() as it's not defined and creates and error in vscode, the example still makes since.
def g(x):
#    if isTuesday():
#        return x + 1
#    else:
        return x

# Definition of a pure function. It's pure as it returns a value based entirely on the arguments. 
def pure_function(x, y):
    temp = x + y*2
    return temp / (2*x + y)

# Definition of an impure function. It's impure because it changes the state of some_list
some_list = []
def impure_function(arg):
    some_list.append(arg)

#########################
# Lambda Functions      #
#########################

# Creating a normal function (using def()) assigns the function to a variable automatically.
# This is different from the creation of other objects such as strings and integers - which can be created on the fly, without assigning them to a variable.
# This on-the-fly creation without assigning a variable is possible with functions as well!
# One condition must be fulfilled, that lambda syntax is used.
# Functions created this way are known as "anonymous functions".
# This is most commonly used when passing a simple function as an argument to another function.

def my_func(f, arg):
    return f(arg)

print("lamba function multiplies input with two and then itself, result is:", my_func(lambda x: 2*x*x, 5))

# Lambdas/anonymous are not as powerful as named functions. They can only do things that require a single expression
# This is usually equivalent to a single line of code.
#(lambda arg: <function definition>)

# Comparison of a named function and a lambda function:

# Named function. We call it by using function_name(argument)
def polynomial(x):
    return x**2 + 5*x + 4
print ("Named function polynomial output with argument -4 is:", polynomial(-4))
# Calling the named function lambda style, with parenthesis around the function!
print ("Named function polynomial output with argument -4 is:", (polynomial) (-4))

# Lambda/anonymous. We call it by a simple trailing (argument) after the lambda definition
print("Lambda function polynomial output with argument -4 is:", (lambda x: x**2 + 5*x + 4) (-4))

# Lambdas can have multiple arguments, defined with (lambda argx, argy: <definnition>)
print ("Multiple argument lambda adds 5 + 5:", (lambda x, y: x + y) (5, 5))

#########################
# Map                   #
#########################

# Map is high-order function that operates on iterables (lists, tuples, generators)
# the map() function takes a function and an iterable as arguments, and return a new iterable (in python 3 it actually returns a map object to be exact),
# with the function applied to each argument.

# Define a simple function for us to use with the map
def add_ten(x):
    return x + 10
# Define a simple iterable, a list
nums = [11, 22, 33, 44, 55]
# Save the return values in the object result. We convert the map object to a list so we can print it later. The map() function takes add_ten and nums as arguments
result = list(map(add_ten, nums))
print("The map function uses function add_ten on all arguments in our list nums, result is:", result)

# We can of course do the same with a lambda function in a simpler (well..) syntax.
# Since map() takes function and argument as arguments it turns into: map(lambda <function>, argument)
# We still have to do the list conversion to be able to print the map object.
print ("lambda function with map adds 10 to all arguments in our list nums, result is:", list(map(lambda x: x + 10, nums)))

#########################
# Filter                #
#########################

# The filter() function is just like map a high order function that operates on iterables (lists, tuples, generators)
# filters an iterable by removing items that don't match a "predicate", a function that returns a boolean.

nums = [11, 22, 33, 44, 55]
# Filter applies the predicate modulus 2 == 0. As such, any numbers that are not even will be false, and hence removed from the return values. 
# I guess the filter returns a filter object, so we have to convert to a list to print it.
result = list(filter(lambda x: x % 2 == 0, nums))
print ("filter() predicate removes all uneven values from nums, result is:", result)

# There were many discussions regarding whether map and filter were usable or not, some say that list comprehensions are the way to go. Perhaps religious.

#########################
# Generators            #
#########################

# Generators are a type of iterable, like lists and tuples.
# Unlike lists, they don't allow indexing with arbitrary indices. But they can still be iterated through with for loops.
# Generators can be created using functions and the "yield" statement.
# The yield statement replaces the return of a function. 
# Yield does not break the loop, unlike "return".
# Yield lets the loop continue until the loop is finished by its conditions. At that end stage it returns the generator object iterable,
# as it was collected and stored during execution in the loop.
# Yielding generates one item at a time. There are no memory restrictions on this, so a generator can in fact be infinite.
# The value of Generators is that they can be used on very large amounts of data, even infinite amounts. 
# This is because they just yield one item at a time, and you don't have to allocate the whole memory allocation for a humungous list or tuple upfront.
# Another value with generators are that performance is increased as generators use on-demand generation of values. We also don't have to wait until all values have
# been generated to start using them, that too increases performance.

def countdown(i):
# Looping for as long as i is greater than 0
    while i > 0:
        # Defining a generator by using yield. We're yielding the value of i, we don't break the loop.
        yield i
        # Just to show that return breaks the loop, we return i when i == 3.
        if i == 3:
            return i
        # count down i step by step
        i -= 1

# We call the countdown function with argument 5. The value returned is a generator object in python3, so we convert to something printable, a tuple.
print ("Call countdown() and print the returned generator object as tuple:", tuple(countdown(5)))
# Just to show that a generator object is returned we print it without conversion
print ("Call countdown() and print generator object without conversion:", countdown(5))

# To display the infinite behaviour or generatorns, consider the below code:

# ###
# def infinite_sevens():
#     while True:
#         yield 7
# for i in infinite_sevens():
#     print (i)
# ###

#########################
# Decorators            #
#########################

# Decorators provide a way to modify functions using other functions. This is ideal when you need to extend the functionality of functions that you dont want to modify.
# print_text is the function we don't want to modify, but we want to decorate it.

# Defining a function with a single argument, a function. This is our decorator that we will use to decorate the print_text function with.
def decor(func):
    # Defining a nested function that will do the decoration.
    def wrap():
        # We do our extra functionality, here we just print some =====
        print("================")
        # We run the actual function that we called decor() with
        func()
        # Extra functionality again, print some more =====
        print("================")
    # The decor() function's return value is the wrap function. All values from the function is returned, here all three lines of strings.
    return wrap

# Define a simple function that will be our argument to the decorator
def print_text():
    print ("Hello World!")

# Declare "decorated" as the decor() with the argument being the print_text function.
decorated = decor(print_text)
# Run decorated, or decor(print_text) to be more exact.
decorated()

# If we had built a real, useful decorator that we always wanted to use to print our text with pretty output, we can replace the print_text function with the
# decorated version. Any time we want to call the function again, we can call the decorated one instead.
# Here we replace the function variable with a function containing the wrapped version.
print_text = decor(print_text)
# Any consecutive calls of the function are decorated
print_text()

# Python provides support to do this with another type of syntax. A pre-pending with a decorator name and the @ symbol.
# Note how a single function can have multiple decorators. We can even re-use the same decorator multiple times.
# We prepend our new function with two decorators (well, it's the same one used twice)
@decor
@decor
# Define our function, no input, just a simple print statement.
def print_text2():
    print ("Hello World again!")
# Run our decorated print_text2 function.
print_text2()

#########################
# Recursion             #
#########################

# Recursion is a very important concept in functional programming. The fundamental part of recursion is self-reference, functions calling themselves.
# Recursion is used to solve problems that can be broken up into easier sub-problems of the same type.
# A classic example of a function that is implemented recursively is the factorial function.
# It finds the product of all positive integers below a specified number.

def factorial(x):
    if x == 1:
        return 1
    else:
        # We multiply our argument with the calling of the function itself and the argument minus 1.
        # This turns into 5 * 4 * 3 * 2 * 1 (note how the recursive call is broken on the last "loop" and 1 is returned as the result to be used in the multiplication)
        return x * factorial(x-1)

print ("Factorial recursion function is given the number 5, 5*4*3*2*1 is:", factorial(5))

# Recursive functions can be infinite. You will be able to run them into a RunTimeError if you run out of recursion depth (meomry).
# That usually happens if you forget to set your "base case", which exits the recursion. Our use case in the example above was 1.

# Recursion can also be indirect. One function can call a second function, that calls the first function, which calls the second, and so on.
# This can occur with any number of functions.

def is_even(x):
    if x == 0:
        # If x is 0 we return true. Note how this can be the result back to is_odd.
        return True
    else:
        # If x is not zero we subtract 1 and return value from is_odd
        return is_odd(x-1)

def is_odd(x):
    # If we send is_even(0) the return is True. With that being return, this functions return is: return not True, i.e. False.
    return not is_even(x)

# The above recursion quickly becomes very complex and there are so many calls back and forth.
# As such, we use minimal numbers below to test the functions.
print (is_odd(0))
print (is_even(1))

# Another tricky example of recursion. For each call when x == 1 or x == 0 we add one to the total return value.
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        # We call recursively to this own function, for each call where x is 1 or 0 our return value will count up by one.
        return fib(x-1) + fib(x-2)
print(fib(4))

#########################
# Sets                  #
#########################

# Sets are data structures, similar to lists or dictionaries. They are created using curly braces or the set() function.
# Quick Repetition reminder of the four data structures in Python:
# tuples are parenthesis, wordtuple = ("spam", "eggs", "sausages", [0, 1, 2],)
# lists are square brackets, wordlist = ["spam", "eggs", "sausages", [0, 1, 2],]
# dictionaries are curly braces and built with pairs, worddictionary = {"Spam": "spam", "eggs": "eggs", "sausages": "sausages"}
# sets are curly braces, num_set = {1, 2, 3, 4, 5}

# Quick guide to when to use which type of data structure:
# When to use a dictionary:
# - When you need a logical association between key:value pair
# - When you need a fast lookup for your data, based on a custom key
# - When you data is being constantly modified. Remember, dictionaries are mutable.

# When to use other types:
# - Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple,
# iterable collection that is modified frequently.
# - Use a set if you need uniqueness for the elements. (they don't do duplicates!)
# - Use tupels when your data cannot change.

# Many time a tuple is used in condition with a dictioanry, for example a tuple might represent a key, because it's immutable.

# Sets share many similaries with lists, such as being able to use len() operation on them.
# However, sets are unordered, like dictionaries, so they can't be indexed.
# Sets CAN'T contain duplicate elements.
# Sets are faster to check whether an item is part of a set, than a list is. This is due to the way data is stored in them.

# Creating a number set with curly braces:
num_set = {5, 4, 3, 2, 1}
# Creating a word set with function set()
word_set = set(["spam", "eggs", "sausage"])

# Much like lists, we can use "in" and "not in" syntax to check the sets if a condition is met.
print ("Check if {0} existis in num_set:".format(3), 3 in num_set)
print ("Checking if \"spam\" is not found in word_set:", "spam" not in word_set)

# We can run operations like len on sets, just like we can on lists.
print("The length of num_set is", len(num_set))

# Some methods differs from lists, such as instead of using "append" method we will use the "add" method
# We use "remove" method to remove a chosen element.
# "pop" method removes an arbitrary element. Perhaps we can say this is true due to the set being ordered for us before printing.
# However, in my tests and what I read is that pop() method will always remove from left to right..
num_set.add(6)
num_set.remove(5)
num_set.pop()
print("We've added 6, removed 5 and popped an arbitrary (well...lefternmost) element, num_set is now:", num_set)

# We can run plenty of mathematical operations on sets to combine them using conditional operators: |, &, -, ^
# | = union operator, combine two sets into a new one containing elements found in either one of them
# & = intersection operator, gets only items found in both sets
# - = difference operator, gets items found in first but not in second
# ^ = symmetric operator, gets items in either set, but not both.

first = {1,2,3,4,5,6}
second = {3,4,5,6,7,8}
print ("\"|\" (Union) of first and second set is:", first | second)
print ("\"&\" (intersection) of first and second set is:", first & second)
print ("\"-\" (difference) of first and second set is:", first - second)
print ("\"^\" (symmetric) of first and second set is:", first ^ second)

#########################
# Itertools             #
#########################

# Itertools is a module in the standard python library. It contains several functions that are useful in functional programming.
# Key functions are:
# One type of function it produces is infinite iterators
# The function count() counts up infinitely from a value
# The function cycle() infinitely iterates through an iterable (for instance a list, string, tuple, generator, anything we can cycle through.
# The function repeat() repeats an object, either infinitely or a specific number of times.

# import function count() from library itertools
from itertools import count
#counting up from 3 to 11
for i in count(3):
    print(i)
    if i >= 11:
        break

# Many functions in itertools that operate on iterables work in a similar fashion to "map" and "filter".
# Remember map and filter that are high-order functions that apply conditions for filtering or altering iterables?
# Examples in itertools are:
# takewhile() - takes an item from an iterable while a predicate function remains true
# chain() - combines several iterables into one long one
# accumulate() - returns a running total  of values in an iterable

#import accumulate() and takewhile() functions
from itertools import accumulate, takewhile
print ("Clarify what we start with a range from 0 to 8:", range(8))
nums = list(accumulate(range(8)))
print("running accumulate() on nums returns an object of the total of all values, iterated for each value:", nums)
print("takewhile() showcases a predicate in play that will stop when x is more than 6 in our list:", list(takewhile(lambda x: x <= 6, nums)))

# Furthermore there are several combinatoric functions in itertools, such as "product()" and "permutaion()".
# These are used when you want to accomplish a task with all possible combinations of some items.

# Import product() and permutations()
from itertools import product, permutations
# Define two letters in a tuple I think since we are using parenthesis. 
letters = ("A", "B", "C")
print (letters, list(range(2)))
print ("output of all possible combinations of A, B, C and 0, 1 is constructed by product():", list(product(letters, range(2))))
print ("All possible permutations of the letters A, B, C with order being significant is found by permutations():", list(permutations(letters)))