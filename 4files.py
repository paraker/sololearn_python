#################################################
#                                               #
# Files                                         #
#                                               #
#################################################

# Before a file can be written to or read from it must be opened, using the open function.
# You can specify the mode used to open a file by applying a second argument to the open function.
# "r" means read mode, the default mode.
# "w" means write mode, for rewriting the contents of a file
# "a" means append mode, for adding new content to a file
# "b" means binary mode, for non-text files such as images or sound files
# You can combine any of the modes with w, such as wb, for write and binary.
# You can also use + to add more modes, such as r+ for read and write, w+ for write and read, and a+ for appending and reading.
# It seems to be equal to write within "<mode>" or mode='<mode>'

#myfile = open ("files/filename.txt", mode='r')
#myfile = open ("files/filename.txt", "r")
#myfile = open ("files/filename.txt", mode='wb')
#myfile = open ("files/filename.txt", "a+")

# Once a file has been opened and used, it should be closed. This is done with the close method
# This is best practice to not have open threads.

#myfile.close()

# Reading files is done with the read method (a method is like a function, but it runs "on" an object)
# the read method takes an arguement which specifies how many bytes of the file to read.
# Consecutive reads of bytes starts where it left off. So if we ead 16 bytes, the next read will start at the 17th byte.
# If no argument is specified, the rest of the file is read.

myfile = open ("files/filename.txt", "r")
#content = myfile.read()
#print (content)
print (myfile.read(16))
print (myfile.read(4))
print (myfile.read())
# Reading an additional line will return an empty string, you're trying to read from the end of the file.
print (myfile.read())
myfile.close()

# There are two methods to read each line of a file. The first one is the function readlines(). It returns a list of each line in the file.
myfileagain = open ("files/filename.txt", "r")
print (myfileagain.readlines())
myfileagain.close()

# We can also read each line with a for loop. The print function automatically adds a new line at the end of its output, as such this will add blank lines between the lines

myfileagain = open ("files/filename.txt", "r")
for eachline in myfileagain:
    print (eachline)
myfileagain.close()

# Writing to a file is done with the write method. Again, a method is like a function, but it's done on an object.
# Note how using the write method does of course delete the file if it excisted. It wil also create it if it doesn't exist.
# If we don't want to do that, we can use append instead, see top of this page for all modes.
# The write method has a return value, the len() of what was written to the file. We can print this return value.

file = open ("files/newfile.txt", "w")
bytes_written = file.write ("Text that will be written to our file")
file.close ()
print ("This is how many bytes that were written:", bytes_written)

file = open ("files/newfile.txt", "r")
print (file.read())
file.close()

# It is good practice to avoid wasting resources by making sure that files are always closed after they have been used.
# One way of doing this is with try, except and finally.

try: 
    file = open ("files/filename.txts", "r")
    print (file.read())
except FileNotFoundError:
    print ("Could not find file")
finally:
    file.close()

# There are a few cases where the error handling of the above is not enough, such in a read error.
# To take it one step further for error handling we can use a larger try block to capture read errors as well.
# A nice way to capture the opening, reading and closing of files explicitly

try:
    # try opening the file
    myfile = open ("files/filename.txt", "r")
    try:
        # Try reading the file
        print(myfile.read())
    except:
        # Handle read errors
        raise
    finally:
        # Close my open files
        myfile.close()
except:
    # Handle open and read errors
    raise

# Another approach of error handling and closing files, on an automatic and perhaps more elegant way, is to use a "with statement"
# The with statement creates a temporary variable (often called f), which is only available in the indented block of the with statement.
# using "with" automatically clears the file variable out of memory after the indented block, even if exceptions occur.
# using the close() method explicitly clears a file variable out of memory, just a more explicit method.
# This is about local and global variables and memory usage, a more advanced topic not yet covered.

with open("files/filename.txt", "r") as f:
    print(f.read())