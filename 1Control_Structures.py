#simple printout
print("## simple output times three ##")
print("hello world")
repeat3 = input("What do you want me to repeat three times?\n")
print (repeat3 * 3)

#while loop, continue goes back to top, break goes out of loop
#We can chuck in an elif statement if we want. The elif is sort of a shortcut of else + and if statement within the else
#you would often have a series of elif statements and then a final else block at the end, to catch anything remaining.
print("\n## while loop with continue and break ##")
i = 0
while True:
    i = i + 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 4:
        print ("We're at 4")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)
print("Finished")

#create list with [], you can put lists in lists. Values count as 0, 1, 2, 3, 4, etc
print("\n## list nested in list ##")
number = 3
things = ["string", 0, [1, 2, number], 4, 56]
print(things[1])
print(things[2])
print(things[2][2]) 
#Strings are immutable lists and they will print a character for you
print("\n## print string as a list ##")
string = "string"
print(string[3])

# You can check true or false in lists with in and not in
print("\n## in or not in ##")
words = ["spam", "eggs", "sausage", "spam"]
print("spam" in words)
print("eggs" not in words)
print("tomato" in words)

# Lists can contain ranges. They must be defined as lists to work. They can take one, two or three inputs and work like this:
numbers = list(range(5))
print(numbers)
numbers = list(range(5,10))
print(numbers)
numbers = list(range(10,20,2))
print(numbers)

# For loops are like foreach loops in most languages
words = ["hello", "world", "spam", "eggs"]
for anything in words:
    print(anything)