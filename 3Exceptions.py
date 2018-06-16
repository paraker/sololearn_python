#################################################
#                                               #
# Exceptions                                    #
#                                               #
#################################################

# When a program fails an exception is thrown, could be from import, index (out of range), name (unknown variable), syntax, type (inappropriate type used), 
# valueerror (inappropriate value called to function) and many others.
# Handling exceptions is particularly useful when you're working with user input, that of course can be something unexpected.
# You can handle exceptions by using try/except statements. The try block containts code that might throw an exception. If the specified exception occurs, the try block
# stops its execution and the exception block is is run.
# An exception statement can list multiple errors, to catch multiple occasions, or even left blank to catch all.
# Note how catching all silently is VERY dangerous and error prone, do avoid this.

try:
    num1 = 7
    num2 = "test"
    print (num1 / num2)
    print ("Done Calculating") 
except ZeroDivisionError:
    print ("An error occurred")
    print ("Due to Zero Division")
except (ValueError, TypeError):
    print ("ValueError or TypeError occurred")

# To ensure some code runs no matter what exceptions are met or not met, you can use a finally statement.
# The code following finally always runs after the execution of the try block, and possibly in the except block/s.
# finally is put at the bottom of the try/except statements.
# Code in the finally block will run even if an uncaught exception occurs!

try: 
    num1 = 7
    num2 = 0
    print (num1 / num2)
except (ValueError, ZeroDivisionError):
    print ("ValueError or ZeroDivisionError occurred")
finally:
    print ("This code will run no matter what")

# You can raise your own exceptions by using a raise statement.
# Hard to see straight away how this can be useful. But it can be used for example with if statements on user input to catch cases you don't want?

num = input (":")
if float(num) > 0:
    raise ValueError("Negative!")
print (1)
#raise ValueError("this is a valueerror!")
print (2)

# We can use the raise without any sstatements in an except statement to re-print the error that was caught

try: 
    num1 = 7
    num2 = 0
    print (num1 / num2)
except (ValueError, ZeroDivisionError):
    print ("ValueError or ZeroDivisionError occurred")
#    raise

# Another testing mechanism is assert, which is a test for the programmer himself. Opposed to exceptions which are used to test external input.
# Assertion is used for internal testing in your code. A sanity check along the way, often used at the start of a function to check for valid input.
# And after a function call to check for valid output.

temperature = -10
# This assert is true, hence nothing happens
assert temperature <= 0
# This assert is not true, it will exit the code with an AssertionError. The second argument will print its string to us at the exit of the error.
assert (temperature >= 0), "Colder than zero!"
# The AssertionErrors can be caught and handled like any other exception with a try/except block. If it isn't handled, the AssertionError will terminate the program.