#################################################
#                                               #
# Regular Expressions                           #
#                                               #
#################################################

# Regular Expressions in python are accessed in the "re" module.

import re

# Definition of a raw string. This is comfortable/good practice to use with regular expressions as raw strings ignore special characters like "\".
# Raw strings is just to avoid confusion with the regular expression characters you will be using.
raw_pattern = r"Hello\nWorld!" # This will be printed as Hello\nWorld!
pattern = "Hello\nWorld!" # Normal string for comparison to the raw string. This will instead have the normal carriage return.

print ("Raw string is:", raw_pattern, "\nNormal string is:", pattern)

# the re function match() checks if the first parameter is found AT THE BEGINNING of the second parameter.
# re.match(Hello\nWorld!, Hello\nWorld!spam). This is true in this case.
if (re.match(raw_pattern, "Hello\nWorld!") and re.match(pattern, "Hello\nWorld!")):
    print("Both raw pattern and normal pattern match \"Hello\\nWorld!\"")
else:
    print("No match")

pattern = r"spam" # Set simple pattern just a raw string "spam"
# re function search() checks if parameter 1 is found anywhere in parameter 2. If true, re.search is True and we will print a sentence.
if re.search(pattern, "rspammy rspammy rspammy"):
    print("re.search() found the string while searching in the whole matching string")
if re.match(pattern, "rspammy rspammy rspammy"):
    print("Pattern found again")
else:
    print("re.match() didn't find this string at the beginning of the matching string")
# re function findall() puts all matches in a list
print(re.findall(pattern, "rspammy rspammy rspammy"))

# re function finditer() works just like findall() but puts the values in an iterable object rather than a list
iterable_object = re.finditer(pattern, "rspammy rspammy rspammy")
for line in iterable_object:
    print(line)

#########################
# search()              #
#########################

# re.search() returns and object with several methods that give details about it.

pattern = r"pam"
matching_pattern = r"eggspamsausage"
search_match = re.search(pattern, matching_pattern)
if search_match:
    print ("search object.group is the matched string: ", search_match.group())
    print ("search object.start is the start position of the match: ", search_match.start())
    print ("search object.end is the end position of the match: ",search_match.end())
    print ("search object.span is the end and start position of the match in a tuple: ",search_match.span())

#########################
# sub()                 #
#########################

# One of the most important re methods that use regular expressions is sub().
# This method replaces all occurrences of the pattern in string with "repl", substituting all occurrences, unless "max" is provided.
# The method returns the modified string.
# Example: re.sub(<search_pattern>, <replacement_string>, <string_to_look_through>, <amount of times to replace, 0 = all>)

str = "My name is Par, Hi Par."
search_pattern = r"Par"
newstr = re.sub(search_pattern, "David", str, 1)
print (newstr)