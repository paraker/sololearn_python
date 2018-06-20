#################################################
#                                               #
# A Simple Game                                 #
#                                               #
#################################################

# Object-orientationis very useful when managing differen objects and their relations.
# That is especially useful when you are developing games with different characters and features.

# Function handling input and simple parsing
def get_input():
    # Asking for user input and splits the string at each space character. This is the default of function split(). If we put something in the parenthesis within quotes that will be the delimeter
    # We store this input in the list command[]
    # i.e. command = "say Hello".split()
    command = input(": ").split()
    # We take the first word from the list command[] and store that in the variable verb_word
    verb_word = command[0]
    # if statemnet to check if the first word in the list is part of the dictionary verb_dict
    if verb_word in verb_dict:
        # We use our word in the list command[] to lookup the value in our dictionary verb_dict{} and store the result in variable "verb"
        # The value stored in the variable is the function say()
        verb = verb_dict[verb_word]
    else:
        # If the first value of command[] does not exist in the verb_dict{} dictionary we print out that we do not know this verb
        print("Unknown verb: {0}".format(verb_word))
        # We exit out of the loop
        return

    # If successful above we continue down to this if statement.
    # It checks if there are more than or equal to 2 values in the list. 
    if len(command) >= 2:
        # We set the second value in the list command[] to variable "noun_word"
        noun_word = command[1]
        # Call of the function stored in the variable "verb". We have stored function say() in this case. The argument for the function is the noun_word variable.
        # i.e. print(say(noun_word))
        print(verb)
        print (verb(noun_word))
    else:
        # If there was fewer than 2 values in the list command[] we call the function stored in variable "verb" with the argument "nothing".
        print(verb("nothing"))

# Definition of a function that is our action to the above command. It takes one argument that we call "noun"
def say(noun):
    # Quick and elegant way of returning a string with single quotes around double quotes to print the actual double quotes without using escape characters 
    return 'You said "{0}"'.format(noun)
    # Alternate way of doing the same but with more familiar syntax as escape characters, double quotes and parenthesis.
    # return ("You said \"{0}\"".format(noun))

# Definition of our verb_dict{} dictionary. We have only defined one value, say, which has the value say(), or more specifically "<function say at 0x03973108>"
verb_dict = {
    "say": say,
}

# To display the menu forever, a while loop returning to the function call of get_input is defined.
while True:
    get_input()