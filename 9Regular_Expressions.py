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
# re function search() checks if parameter 1 is found anywhere in parameter 2.
if re.search(pattern, "rspammy rspammy rspammy"):
    print("re.search() found the string while searching in the whole matching string")
if re.match(pattern, "rspammy rspammy rspammy"):
    print("Pattern found again")
else:
    print("re.match() didn't find this string at the beginning of the matching string")
# re function findall() puts all matches in a list
print(re.findall(pattern, "rspammy rspammy rspammy"))
iterable_object = re.finditer(pattern, "rspammy rspammy rspammy")

for line in iterable_object:
    print(line) 