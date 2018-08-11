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

#########################
# match()              #
#########################

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

#########################
# Metacharacters        #
#########################

# Metacharacters make regular expressions more powerful than regular strings.
# There can be a lot of escaping when using metacharacters. To get around this, you can use raw strings, that are exactly what they look like.

# . matches any character
# ^ start of string, $ end of string
# | = or. (a|b) matches a or b

# Repetition metacharacters:
# * = 0 or any repitition of the previous thing, the previous thing can be a single character, a class or a group of characters in parenthesis ().
# + = 1 or more repetitions of the previous thing
# ? = 0 or 1 repetition of the previous thing
# {} can represent the number of repetitions between two numbers. {1,3} means between 1 and 3 repetitions of the previous thing.

search_pattern = r"9{1,3}$"
if re.match(search_pattern, "999"):
    print ("Match 999")
if re.match(search_pattern, "9999"):
    print ("Match 9999")

#########################
# Character classes     #
#########################

# Character classes provide a way to match only a specific set of characters. The class is defined by square brackets[].

search_pattern = r"[aeiou]"
if re.search(search_pattern, "grey"):
    print ("any character in \"aeiou\" is found in \"grey\"")

# We can group classes together
search_pattern = r"[A-Z][A-Z][0-9]"
if re.search(search_pattern, "FF9054"):
    print ("Upper-case, Upper-case + a digit was found in the string")

# a "^" at the start of the class inverts it. i.e. [^A-Z] excludes upper-case letters, but matches ANYTHING else!
search_pattern = r"[^0-5]"
if re.search(search_pattern, "FF9054"):
    print ("Anything else than numbers 0-5 was found in the string")

#########################
# Groups                #
#########################

# Groups are created with parenthesis. It groups a section of a pattern together for a more precise match. The groups can be nested.
# We can later access the groups by the .group() method.
search_pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(search_pattern, "abcdefghijklmnop")
if match:
    print(match.group()) # return the whole match
    print(match.group(0)) # return the whole match
    print(match.group(1)) # return group 1
    print(match.group(2)) # return group 2
    print(match.groups()) # return all groups

# There are special groups, named groups and non-capturing groups.
# Named groups are defined by "?P<name>..." where <name> is the name of the group and ... is the pattern.
# Non-capturing groups are defined by "?:..."

search_pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(search_pattern, "abcdefghi")
if match:
    print("We're printing the group \"first\":", match.group("first"))
    print("We're printing all printable groups:", match.groups())

#########################
# Special Sequences     #
#########################

# There are various special sequences that are expressed as backslash followed by another character.

# \any_number such as \1 or \17 matches the expression of the group of that number
search_pattern = r"(.+) \1"
match = re.match(search_pattern, "word word")
if match:
    print("Match \"word\" and then use that value to match the next word")
match = re.match(search_pattern, "abc cde")
if match:
    print("Match \"abc\" and then use that value to match the next word, which will be missed here")

# \d = digit = [0-9]
# \s = whitespace = [\t\n\r\f\v]
# \w = word characters = [a-zA-Z0-9] and any unicode character such as åäö
# the uppercase use of them inverts them, \D matches anything BUT [0-9]

# Special sequences are \A, \Z and \b.
# \A matches the beginning of a string, \Z matches the end of a string,
# \b matches the boundary between words, any characters that isn't \w or \W, can match space, <>!)%@#% and so on.

search_pattern = r"\b(cat)\b"
match = re.search(search_pattern, "s<cat<tered")
if match:
    print("We matched word boundary+cat+word boundary")

#########################
# Email Extraction      #
#########################

# Sample usage of regex to extract emails.
# our goal is to extract the string info@sololearn.com from this string:
str = "Please contact info@sololearn.com for assistance"
str2 = "Please contact info@sololearn.com.au for assistance"
# An email address consists of a word that may include dots and dashes, followed by @ and the domain name + suffix.

search_pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
# ([\w\.-]+) matches any word character, dot and dashes, one or more number of times.
# @ matches @
# same pattern again, looking for one of more instance of word characters, dots and dashes
# (\.[\w\.]+) matches a dot, then any word character and dots, one or more times.
match = re.search(search_pattern, str)
if match:
    print(match.group())
match = re.search(search_pattern, str2)
if match:
    print(match.group())

#########################
# Lookbehind            #
#########################

# https://docs.python.org/3/library/re.html
# Matches if the current position in the string is preceded by a match for ... 
# that ends at the current position. This is called a positive lookbehind assertion.
# (?<=abc)def will find a match in 'abcdef',
# since the lookbehind will back up 3 characters and check if the contained pattern matches.

m = re.search('(?<=abc)def', 'abcdef')
m.group(0)

# This example looks for a word following a hyphen:

m = re.search(r'(?<=-)\w+', 'spam-egg')
m.group(0)
'egg'