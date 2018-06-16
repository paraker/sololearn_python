#################################################
#                                               #
# Text Analyser                                 #
#                                               #
#################################################

# Example project showing a program to find what percentage of the text each character occupies.

# Define a function that counts how many times a character occurs in a string
# Note that there is already a python built-in function for this of course, called ".count()"
# But the lesson here is obviously to understand what we're doing
def count_char(text, char):
    """
    Below code takes text and counts amount of character that we name?
    """ 
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

# We open the file using with, the indented block determines what happens before the file is automatically closed.
# Using a while loop to display the input "menu" again if we didn't find the file we searched for
while True:
    filename = input ("Which file do you want to anyalyse?\n")
    try:
        # Try opening the file
        with open("files/" + filename, "r") as f:
            try:
                # Try reading the file
                file = f.read()
                # Break out of while loop if read successfully
                break
            except:
                print ("couldn't read or call counting function")
                # Go back to reading for a new file with continue
                continue
    except FileNotFoundError:
        print ("File not found, please try again")
        # Go back up to top, asking for a new file to read
        continue

# for loops in python are like foreach loops.
# We iterate through the lowercase alphabet by giving a for loop a string of all lowercase characters.
# The indented block is executed once per character, so a, b, c,d and so on. Also printing a space just for fun.
# This is very, very inaccurate as we don't count for punctuation, uppercase characters etc... 
print ("This is the file we will analyse: \n", file)
# Iterate through each lowercase character in the alphabet, run through the indented block each time.
for letter in "abcdefghijklmnopqrstuvwxyz ":
    # Count percentage per letter using our own function
    percentage = 100 * count_char(file, letter) / len(file)
    # Count percentage per letter using pythons built-in function
    percentage_python = 100 * file.count(letter) / len(file)
    # Print each letter - percentage using the format function. Format function is a great way to mix strings and variables, floats, integers etc
    # round() sets the amount of decimals as per the second arguement, rounded up or down to the closest decimal as specified.
    print ("{0} - {1}%".format(letter, round(percentage, 2)))
    print ("{0} - {1}%".format(letter, round(percentage_python, 2)))