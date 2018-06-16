#################################################
#                                               #
# More Types                                    #
#                                               #
#################################################

#########################
# "None" object         #
#########################

# It's the equivalence of null in other programming languages.
# it is used to represent the absence of a value, such as 0, [] and the empty string.
# None is false when converted to a boolean. 
print(bool(None))

# None is False in if statemnents
if None:
    print("None is interpreted as True")
else:
    print("None is interpreted as False")

# None is printed out as None, the absence of a value
print(None)

# Any function that doesn't have a specified return value, None is returned.
def my_function():
    print("Hello World")
print(my_function())

#########################
# Dictionaries          #
#########################

# Dictionaries are data structures used to map arbitrary keys to values. Equivalent to maps in terraform and hash in other languages.
# It can be thought of as a dictionary, where we use a key or keyword to lookup a value.
# Dictionaries are defined with curly brackets, double quoted keys: values, separated by comma
# Only immutable objects (strings, integers, bool, float) can be defined as keys to dictionaries. The only mutable objects we've come across so far are lists and dictionaries.
# If we try to define a mutable object as a key we will receive a TypeError.
# If we want to print all keys, values or items in a dictionary, we use the corresponding keys, values and items methods

ages = {"Dave": 24, "Mary": 42, "Tom": 33}
print (ages["Dave"])
print (ages.keys())
print (ages.values())
print (ages.items())

# An unknown key call will result in a key error
try:
    print (ages["Par"])
except KeyError:
    print ("We got ourselves a KeyError here")

# We can loop through a dictionary with a method to print all values.
for anything in ages.values():
    print (anything)

# The order of the items in a dictionary is arbitrary to the code. It means that operations the order in which you see the values doesn't matter.
# We can change the values of the keys and we can add new items to dictionaries.  

fruit_prices = {"Banana": 2, "Apple": 1, "Citrus": 3}
fruit_prices ["Cucumber"] = 0.1
fruit_prices ["Banana"] = 3
print (fruit_prices.items())

# To determine whether a key is in a dictionary, we can use "in" or "not in", just like you can for a list

print ("2" in fruit_prices)
print ("Banana" in fruit_prices)

# To get values from a dictionary we use the method get. If the get method doesn't find the key specified by you it return "None" by default.
# Alternatively you can explicitly tell get to return something else.

print (fruit_prices.get("Banana"))
print (fruit_prices.get("Orange"))
print (fruit_prices.get("Orange", "This is the custom output if not found"))

#########################
# Tuples                #
#########################

# Tuples are very similar to list, except that they are immutable, i.e. they cannot be changed. They process faster than lists.
# Tuples are created by using parenthesis as opposed to square brackets used by lists. If you want you can leave the parenthesis out as well.
# The potentially mutable values within a tuple can change however, if you really want them to.
# Tuples are ordered of course and we get values by using numbers starting from 0, just like in lists.

wordtuplewithoutparenthesis = "spam", "eggs", "sausages", [0, 1, 2]
wordtuple = ("spam", "eggs", "sausages", [0, 1, 2],)
wordlist = ["spam", "eggs", "sausages", [0, 1, 2],]
worddictionary = {"Spam": "spam", "eggs": "eggs", "sausages": "sausages"}
print (wordtuple, wordlist, worddictionary, wordtuplewithoutparenthesis)
# Just a silly example that the valeus in the tuple are still mutable
wordtuple[3][2] = "New Value"
print (wordtuple[3][2], wordlist[3][2])

# Tuples are as we said immutable and we get TypeError if we try to change values.
try:
# I comment out the below line otherwise vscode python linting marks the code as erronous and makes the file red :).
 #   wordtuple[0] = "cheese"
    wordlist[0] = "cheese"
except TypeError:
    print ("We received a type error here")
finally:
    print (wordlist[0])

#########################
# List Slices           #
#########################

# List slices provide a more advanced way of retrieving values from a list or a tuple. Basic slicing is done by indexing list using two colon separated integers.
# The first integer is included in the result, the second isn't.
# More advanced slicing is done with three comma-separated integers. The third value indicates how many "steps" between the chosen values in the list (or tuple).
# If we leave out the first integer, we start from the beginning of the list.
# If we leave out the second one we stop at the end of the list.
# If we leave out the third we use single steps.
# Basically, yourlist[start(default 0):stop(default end of list):step(default 1)]

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print (squares[0:1])
print (squares[2:7:2])
print (squares[:3])
print (squares[3:])

# If we use negative values in the first or second integer, we count backwards from the end of the list.
# Start below is five steps back from end of list.
print (squares[-5:])
# And below stop is three steps back from the end.
print (squares[:-3])

# Lastly, if the third value is negative, the slicing is done backwards.
# You can if you wish as such, reverse a whole list by yourlist[::-1]. This can also be done with the reverse method, but more on that somewhere else.
print (squares[::-3])

#########################
# List Comprehensions   #
#########################

# List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
# We set the condition to what we want and use "for <variable> in range(x)"
# In this example we simply multiply the variable in a list with values 0-4
cubes = [i*2 for i in range(5)]
print (cubes)

# List comprehensions can also use if statements by simply adding on any number of if statements in the list comprehension expression.
# We create an if statement the specifically tells the list comprehension to only allow the variables that leave 0 over when divided by 2.
# This filters out some other values in our list comprehension. I created the full list side by side for comparison. 
evens = [i**2 for i in range(10) if i**2 % 2 ==0]
evenswithoutif = [i**2 for i in range(10)]
print (evens)
print(evenswithoutif)

# If you try to create too long list comprehensions you'll be thrown a MemoryError. To create extensive lists we must instead use generators, which will be covered later.

#########################
# String Formatting     #
#########################

# So far, to combine non-strings and strings we've converted non-strings to strings and added them.
# String formatting provides a more powerful way to embed non-strings with strings. String formatting uses a string's format method
# to substitute a number of arguments in the string.

# Each argument to the format method is placed in the string at the corresponding position, which is determined by the curly braces.
nums = [4, 5, 6,]
msg = "Numbers: {0} {1} {2}".format (nums[0], nums[1], nums[2])
print (msg)
# The order of the curly braces don't have to be in order. You can also use any other values for the indices, let's put in a string here as example.
msg = "Numbers: {2} {0} {1}".format (nums[0], "string", nums[2])
print (msg)
# We can also re-use values from the format method.
print("Magic tricks while saying: {0}{1}{0}".format("abra", "cad"))
# We can also use named arguments, here we pull x and y that are defined straight in the format method.
print("x is {x}, y i {x}".format(x=5, y=12))

#########################
# String Functions      #
#########################

# Python contains many useful built-in string functions and methods to accomplish common tasks.
# join - joins a list of strings together with another string as a separator.
# replace - replaces a substring in a string with another.
# startswith & endswith - determine if there's a substring at the start or at the end of a string, respectively.
# lower and upper - changes the case of the characters in a string
# split - opposite of join, turns a string with a certain separator into a list.

# We call the join method on the " and " string which is our separator. The list with spam eggs and ham is joined with the separator in between each value/string.
print (" and ".join(["spam", "eggs", "ham"]))

# Apparently the replace method can only take three arguements, so in this example I tried calling it twice, which seemd to work.
# It seems to take the first string and replace it with the second string.
print ("Goodbye ME".replace("ME", "World").replace("Goodbye", "Hello"))

# Checking if the string starts with "This". If it does, startswith prints out True.
# Also checking if mystring ends with "string"
print ("This is a string".startswith("This"))
mystring = "This is a string"
print(mystring.endswith("string"))

# Syntax of upper and lower:
print("this sentence will be so loud".upper())
print("I'M WHISPERING!".lower().replace("!", " *schhh*"))

# The split function's argument is the separator that determines where the split for the list will be, much like awk I guess.
# It also looks like the separator is consumed by the split function, only saving what's not in the separator in the list.
print("spam, eggs, ham".split(", "))
print ("Spam#^Eggs#^Ham".split("#^"))

############################
# Numeric String Functions #
############################

# To find the maximum or minimum of some numbers or a list, you can use the max and min functions
# abs shows how far from 0 a value is, and sum sums all the values in a list.
print ("Minimum value of these numbers is:", min(1, 2, 4, 6, 8, 0))
print ("Maximum value in this list is:", max([1, 2, 4, 6, 8, 0]))
print ("Absolute value is (\"how far away is this number from 0\"):", abs(-99))
print ("The total value (sum) of this list is:", sum([1,3,5,-8,13]))

############################
# List Functions           #
############################

# List functions are often used in conditional statements.
# "all()" and "any()" functions take a list as an argument and return True if all or any (respectively) of their arguments evaluate to True,
# "enumerate()" function can be used to iterate through the values and indices of a list simultaneously.

nums = [55, 44,33, 22, 11]
if all([i > 5 for i in nums]):
    print("All numbers in nums are greater than 5")
if any([i % 2 == 0 for i in nums]):
    print ("At least one number in nums is equal")

# enumerate() list the indices and the values in a list:
for v in enumerate(nums):
    print(v)