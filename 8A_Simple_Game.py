#################################################
#                                               #
# A Simple Game                                 #
#                                               #
#################################################

# Object-orientationis very useful when managing differen objects and their relations.
# That is especially useful when you are developing games with different characters and features.
# We're creating a simple classic, an adventure text-based game.

# Creating a superclass to represent game objects. 
class GameObject:
    # Definition of attributes in the GameObject class that will be referenced later. Two strings and one dictionary.
    class_name = ""
    desc = ""
    objects = {}

    # Defintion of __init__ magic function that will be called upon instantiation of the class. Takes variable name as argument.
    def __init__(self, name):
        # Sets the attribute name for the object we passed to the class, i.e. goblin.name = Gobbly
        self.name = name
        # This line maps a value in the dictionary objects{}. It references the object we passed to the class  
        # GameObject.objects[goblin.class_name] = goblin
        # I set the class_name to goblin_class_name to be a bit more clear to what's being referred. It makes the game input/output code quite silly.
        # it becomes silly becuase we don't lookup the value of the dictionary, we lookup the class_name itself (and also the description).
        # it would be better to lookup the corresponding value in the dictionary, wouldn't it?
        # GameObject.objects[goblin_class_name] = goblin
        GameObject.objects[self.class_name] = self
    
    # Definition of function get_desc that takes one argument, the object passed to the class?
    def get_desc(self):
        # return __main__Goblin object.class_name + new line + __main__Goblin object.desc
        return self.class_name + "\n" + self.desc
    
# Creation of subclass Goblin, masterclass is GameObject.
class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self.desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >=3:
            return self._desc
        elif self.health == 2:
            health_line = "It has awound on its knee."
        elif self.health == 1:
            health_line = "Its arm has been cut off."
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line
    
    @desc.setter
    def desc(self, value):
        self._desc = value

# Instantiate an object of the class Goblin(), passing the argument "Gobbly", store the result in "goblin"
goblin = Goblin("Gobbly")

####################################
# Variables definition             #
####################################

# The first variable we give the game is "verb", verb here is "examine". It takes one argument, a "noun" which is the second input from the user.
def examine(noun):
    # if <second argument from user> exists in GameObject.objects{} dictionary, then
    if noun in GameObject.objects:
        # Return GameObject.objects{goblin_class_name}.get_desc()
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here".format(noun)

# Definition of a function that is our action to the above command. It takes one argument that we call "noun"
def say(noun):
    # Quick and elegant way of returning a string with single quotes around double quotes to print the actual double quotes without using escape characters 
    return 'You said "{0}"'.format(noun)
    # Alternate way of doing the same but with more familiar syntax as escape characters, double quotes and parenthesis.
    # return ("You said \"{0}\"".format(noun))

# Definition of the combat move hit
def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here".format(noun)
    return msg

# Definition of our verb_dict{} dictionary. We have only defined one value, say, which has the value say(), or more specifically "<function say at 0x03973108>"
verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit,
}

###############################################
# Function handling input and simple parsing  #
###############################################

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
        print (verb(noun_word))
    else:
        # If there was fewer than 2 values in the list command[] we call the function stored in variable "verb" with the argument "nothing".
        print(verb("nothing"))



# To display the menu forever, a while loop returning to the function call of get_input is defined.
while True:
    get_input()