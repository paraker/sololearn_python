#################################################
#                                               #
# Object-oriented Programming                   #
#                                               #
#################################################

# We have previously looked at two paradigms of programming:
# Imperaive - using statements, loops and functions as subroutines
# Functional - using pure functions, high order functions and recursion

# A third, very popular paradigm is object-oriented programming (OOP)
# Objects are created using classes, which are he focal point of OOP.
# The class describes what the object will be, but is sepaate from the object itself.
# In other words, a class can be described as an object's blueprint, description or definitoin.
# You can use the same class as a blueprint for creating multiple different objects.

# Classes are created using the keyword "class" and an indented block, which contains class methods (which are functions)

class Cat:
    # we define a class method called __init__. Remember that class methods are functions!
    # the "self" argument refers to the object itself that was passed onto this class. The other two arguments are what was passed to the class as arguments
    def __init__(self, color, legs):
        #self.color = felix.color = ginger
        self.color = color
        #self.legs = felix.legs = 4
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

#########################
# __init__ method       #
#########################

# the __init__ method is the most important method in a class
# This is called when an instance (object) of the class is created, using the class name as a function.
# All methods must have "self" as their first parameter, although it isn't explicitly passed.
# Python adds the self argument to the list for you, you don't need to include it when you call the methods.

#########################
# other methods         #
#########################

# Classes can have other methods defined to add functionality to them. Remember, all methods must have "self" as their first parameter.
# Methods are accessed using the same "dot.syntax" as attributes

# Classes can also have "class attributes", created by assigning values within the body of the class. 
# These can be accessed either from instances of the class, or the class itself.

class Dog:
    # Below "legs = 4" is a class attribute. I guess a static definition of an attribute in this case.
    legs = 4
    # Mandatory __init__ method
    def __init__ (self, name, color):
        # fido.name = Fido
        self.name = name
        # fido.color = Brown
        self.color = color

    # Defining a method to add functionality to the class. The mandatory "self" parameter is used.
    def bark(self):
        return "Woof"
        

# We create object fido, of the class Dog, sending arguments "Fido" as name, and "Brown" as colour.
fido = Dog("Fido", "Brown")
# We call for object fido's name
print ("the name of object fido is:", fido.name)
# The "other method" that was defined in the class is put into the object. It's called by the normal dot syntax.
print ("When we call the bark method from Dog class Fido goes:", fido.bark())
# We can access the class attribute of the class itself
print("attribute \"legs\" of class Dog is:", Dog.legs)
# And also access the class attribute of our object
print("attribute \"legs\" of object fido is:", fido.legs)


########################################
# Inheritance/superclass/subclass      #
########################################

# Inheritance provides a way to share functionality between classes. Imagine several classes, Cat, Dog, Rabbit and so on.
# Although they may differ in some ways (only Dog may have method bark()), they are likely to be similar in others
# (all having the attributes color and name).
# This can be expressed by making them all inherit from a "superclass Animal", which contains the shared functionality.
# To inherit a class from another class, put the superclass name in parenthesis after the class name
# If we want to get the methods from a superclass in a subclass we can use the function super().

# superclass Animal is defined as a normal class
class Animal:
    def __init__ (self, name, color):
        self.name = name
        self.color = color
        self.legs = 4
    
    def sound(self):
        return "Standard animal sound"
    
    def size(self):
        return "Standard animal size"

# Definition of subclass Rabbit, inheriting of the superclass Animals' attributes is specified by putting the superclass in parenthesis
class Rabbit(Animal):
    # We define an "other method", to add a unique element to the Rabbit class.
    def squeak(self):
        print("squeak!")

# We create a rabbit with the object bunnyhopper
bunnyhopper = Rabbit("Bunnyhopper", "white")
# Print bunnyhopper object's name that was defined in the superclass, but used in the subclass.
print (bunnyhopper.name)
# Use the subclass' unique method squeak.
bunnyhopper.squeak()

# If a subclass inherits methods or attributes that are also defined in the subclass, i.e. and overlap with the same name, the subclass' defintion wins, it overrides the inheritance.
# Defining a new subclass Ostrich, using the superclass in the parenthesis.
class Ostrich(Animal):
    # Definition of an int method that will be called upon creation of the object that we pass to the class
    def __init__(self, name, color):
        # We use name and color from the superclass, but we override the legs parameter by setting it in the subclass
        self.legs = 2
    def size(self):
        return "Large"
    
# Create an ostrich which gets name and color from superclass Animal and amount of legs from subclass Ostrich.
donald = Ostrich("Donald", "White and Black")
# Print amount of legs to show that the subclasses' arguments and methods override the superclass'
print("Donald has his many legs:", donald.legs)

# Inheritance can continue from a subclass to another subclass, and continue that way in multiple inheritances. However, You can't have circular inheritance.
# Definition of a subclass of a subclass. The DwarfOstrich is an Animal, and and Ostrich and a DwarfOstrich.

class DwarfOstrich(Ostrich):
    # Defition of a function that overrides previous inheritance of method size()
    def size(self):
        # Return a string for printing
        return "Tiny"
    # Definition of a method that will point to the first-in-line superclass (the subclass Ostrich)
    def supersize(self):
        # Call to the superclass' method size(). This equates to Ostrich().size(), at least I think so. This does only seem to be avaialble for the direct parent, not the superclass of the superclass.
        return super().size()

# Creation of object from a subclass of a subclass.
dwarf_donald = DwarfOstrich("Donald the Dwarf", "Black and White")
# Print of the direct subclass' method.
print ("How big are you, Donald the dwarf?", dwarf_donald.size())
print ("How big would you be, if you were of your parent's class, Donald the dwarf?", dwarf_donald.supersize())
# Print of the superclass' method, shows that inheritance has come all the way through from superclass to subclass to subsclass.
print("This is how the dwarf ostrich sounds:", dwarf_donald.sound())

#########################################
# Magic Methods / dunders / overloading #
#########################################

# Magic methods are special methods which have __double underscores__ around them. They are also known as dunders.
# So far, the only one we've seen is the __init__ method, but there are many others.
# The magic methods are used to create functionality that can't be represented as a normal method.

# One common use of the magic methods is operator overloading. This means defining mathematical or other operators that can be used on objects from custom classes.
# Examples of mathematical magic methods are __add__ for +, __sub__ for -, __mul__ for *, __truediv__ for / etc.
# The truth is that behind the scenes in the C code, python actually interprets the sybmols +, -, * etc as __add__, __sub__ etc.
# So what we're doing here for our custom classes is that we're re-defining the meaning of the operators.
# As we've designed the classes ourselves it's not obvious to python how it should deal with the objects we have defined. Should it return a string? a bool?
# Should it add? Should it use str operations?
# To help python understand what we want to do mathematically we do operator overloading with the magic methods.

# Just to show an example of that what python is actually seeing when we type - is __sub__. We can print out the actual syntax and it works the same way!
value1 = 3
value2 = 1
# Using the actual interpreted syntax of python for subtraction:
value3 = value1.__sub__(value2)
print ("Still the same subtraction, regardless of syntax!", value3)

# Defining a class Vector2D
class Vector2D:
    # the magic method __init__ is called when an object is passed to the class
    def __init__(self, x, y):
        # object.x = x
        self.x = x
        # object.y = y
        self.y = y
    
    # Definition of the magic method __add__ which will respond to operations with "+" on objects from our Vector2D class.
    def __add__(self, other):
        # We return a Vector2D object calculated from the two passed objects as arguments, as we have defined it here with simple addition.
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        # Here we will mess up the subtraction sign by using multiplication instead of subtraction.
        return Vector2D(self.x * other.x, self.y * other.y)

# Create a Vector2D object called "first".
first = Vector2D(5, 7)
# Creat another Vector2D object, called "second"
second = Vector2D(3, 9)
# Define "result" as the return value from first __add__ second. "result" becomes a Vector2D object.
result = first + second
# Print the x value of the Vector2D object result.
print ("The first two values in our vectors combined is:", result.x)
# Print the y value of the Vector2D object result.
print ("The second two values in our vectors combined is:", result.y)

# Redefine the Vector2D object result by assigning it the values of first __sub__ second.
# Note how we've defined sub to be multiplication instead of subtraction.
result = first - second
# Print the x value of the Vector2D object result.
print ("The first two values in our vectors subtracted is:", result.x)
# Print the y value of the Vector2D object result.
print ("The second two values in our vectors subtracted is:", result.y)

# There was a section on reversed magic methods that wasn't explained. It said that if an object hasn't implemented the magic function
# we're trying to use and the two values you're trying to perform operations on are of different types, python will reverse the operands
# and try again. There reversed magic methods are called __radd__, __rsub__ and so on. 
# This thesis didn't work when I tried it. Massive confusion on sololearn too. Move on.

# Comparison methods are following the same principle. Their interpreted versions are __lt__ for <, __le__ for > and so on!
if (value1.__ge__(value2)):
    print ("value1 is greater or equal than value2")

# There are magic methods that can overload other functionality, not just mathematics.
# We can for example overload indexing with __getitem__, __len__ for len(), __iter__ for iteration over objects (i.e. in for loops).
# At this stage, it's good to know that you can basically overload anything you want in your custom classes.
# This is good to use when you need a custom rule for your operations on custom object, say perhaps in your iterations you always want to skip every other item or something similar.
# you only have to overload the __iter__ operation once for that class. Every time you call it this will then happen automatically.

