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


#########################################
# Object Lifecycle / Garbage Collection #
#########################################

# The lifecycle of an object is made up of it's creation, manipulation and destruction.
# The first stage of the creation is the definition of the class of which it belongs to.
# Second stage is instantiation of an instance, when __init__ is called.
# Memory is then allocated to store the instance. Just before this occurs, the __new__ method of the class is called, this method is very rarely edited.
# The object is now ready to be used and other code can interact with the object and use its variables.
# Eventually, it will finish being used and the object can be destroyed.

# Destruction of an object occurs when its reference count reaches zero. Reference count is the number of variables and other elements that refer to an object.
# In some situations, two (or more) objects can be referred to by each other only, and can therefore be deleted as well.
# There is a magic method to reduce the number of reference count by one, this magic method is __del__.

# The process of deleting objects when they are no longer needed is called "Garbage Collection".
# In summary, an object's reference count goes up when it's assigned a new name, or placed in a container (list, tuple or dictionary).
# The object's reference count decreases when it's deleted with __del__ or when the reference goes out of scope.
# When an object's reference count reaches zero, Python automatically deletes it by garbage collection

a = 42 # Create an object <42>
b = a # Increase reference count of <42>
c = [a] # Increase reference count of <42>

del a # Decrease reference count of <42>
b = 100 # Decrease reference count of <42>
c[0] = 1 # Decrease reference count of <42>
# Python will now garbage collect object <42>

#########################################
# Data Hiding                           #
#########################################

# A key part of object-ortiented programming is encapsulation. Many functions and variables into a single easy-to-use object (an instance of a class).
# A related concept is "data hiding". The details of a class is to be hidden and a clean standard interface is presented for those who wants to use the class.
# In other programming languages this can be done with private methods and attributes, which have their external access blocked.
# However, in python there is a different philosophy. It is "we are all consenting adults here", meaning that you should not (and can't) put
# arbitrary restrictions on accessing parts of a class. Instead, the python developers use discouraging context to shy people away from editing private portions.

# The discouraging context in python is done with single underscores before methods and attributes.
# This means that no external code should be using these methods or attributes.
# However, this single underscore is a convention and does not actually stop external code from accessing the method or attribute.
# The single underscore does however stop the asterisk import from a module to include the (weakly) private variables.

# Define a class called Queue
class Queue:
    # Instantiation of the object with the dunder/magic method __init__ that is called upon calling of the class.
    def __init__(self, contents):
        # the "contents" argument is stored in the instantiated self-argument. The weakly private method _hiddenlist is defined with a single underscore.
        self._hiddenlist = list(contents)
    
    # Definition of push() function with the weakly private method _hiddenlist. 
    def push(self, value):
        # We insert a value at place "0" in the list.
        self._hiddenlist.insert(0, value)
    
    # Definition of pop() function with weakly private method _hiddenlist
    def pop(self):
        # We pop(), i.e. take away the value at place "0" in the list
        return self._hiddenlist.pop(0)
    
    # Definition of magic function __repr__. This is a string representation of an instance of our class Queue.
    def __repr__(self):
        # We use format to print the _hiddenlist
        return "Queue({0})".format(self._hiddenlist)

# Call class Queue, instantiate an object and store it in variable "queue"
queue = Queue([1, 2, 3])
print(queue) # Print our queue.
 # Call the function push() with the weakly private attribute in it. This would be normal operation.
 # Pop the integer 4 into slot "0" in the list
queue.push(4)
print(queue) # print our queue again to show the new integer
# Call the function pop() with the weakly private attribute in it. This would be normal operation.
# It will remove the newly introduced integer from the list
queue.pop()
print(queue) # print the list again
# We call the weakly private attribute directly from outside code. This is not advised, but see, it's working!  
print(queue._hiddenlist) 

# There is a higher level of discouraging as well, a convention for strongly private methods and attributes.
# This is done with a double underscore at the beginning of their names.
# This cause the names to be mangled, which means that they can't be accessed from outside the class.
# The purpose is not to ensure that they are kept private, but to avoid bugs if there are subclasses that have
# methods or attributes with the same names.
# Name mangled methods can still be accessed externally, but by a different name. For this, we use "_<class_name>__stronglyprivatemethod"
# Bascially, the mangling that's happening in the background is that Python adds _<class_name> in front of the strongly private method/attribute!

class Spam:
    # Strongly private attribute __egg = 7.
    __egg = 7
    # Definition of function "print_egg()"
    def print_egg(self):
        # Print the instantiated object's __egg attribute.
        print(self.__egg)

# Instantiate an object from the class Spam, store it in variable "s"
s = Spam()
# Call the function print_egg() to print the __egg attribute of "s"
s.print_egg()
# We use the special syntax "_<class_name>__stronglyprivatemthod" to print the storngly private attribute __egg
# I've commented this out because pythonlint in vscode does not like it one bit!
#print("The strongly private attribute of __egg is:", s._Spam__egg)
# Attempt to print the strongly private attribute __egg. This fails with Attribute Error. Why? Because the mangling changes the name for external code, to _Spam__egg!
try:
    print(s.__egg)
except AttributeError:
    print ("We could not print this attribute. (We know it's stringly private, that's why)")

#########################################
# Class Methods                         #
#########################################

# Methods of objects we've looked at so far are called by an instance of a class, which is then passed to the .self parameter of the method.
# Class methods are different, they are called by a class, which is passed to the cls parameter of the method.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

# To be able to use cls ("class self-variable") we need a decorator. The @classmethod is a decorator.
# What's a decorator again? Have a look at 7Functional_Programming. We used it before to print stuff pretty.
    @classmethod
    # We define this type of method to make like simpler when calling for a new type of object that has specific requirements.
    # For example, if we wanted to make a square and not a rectangle, we can call this classmethod directly and only have to type one argument.
    # May not be a big deal, but this can of course grow more complex in other examples.
    # This method takes ONE argument and passes on TWO arguments to the pre-defined class-constructor. It knows which class-constructor
    # to pass these arguments to by the <Class_name>.method() calling of the instantiation.
    # This is called a "Factory Method". 
    def new_square(cls, side_length):
        # Pass return values to the class-constructor Rectangle. Rectangle(5,5)
        return cls(side_length, side_length)

# Instantiate an object "square" of the class rectangle, width 2, height 6
square = Rectangle(2,6)
# Use the class method calculate_area() on square, this will print 12.
print ("Our first rectangle has the area:", square.calculate_area())
# Instantiate an object "square" of the class Rectangle on the classmethod "new_square()".
# We only need to pass one parameter here, as the classmethod only takes one argument, the length of the side of the square.
# We know the class-constructor is Rectangle, this is where the return arguments will be passed to.
square = Rectangle.new_square(5)
# The object is still of the class Rectangle and we can use the class method calculate_area() to calculate the area. This now turns into 5x5=25.
print("Our square has the area:", square.calculate_area())

#########################################
# Static Methods                        #
#########################################

# Static methods are similar to class methods, except they don't receive any additional arguments. They are identical to normal functions that belong to a class.
# They are marked with the staticmethod decorator.

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    # Definition of static method validate_topping(). Again, we need to use a decorator @ to be able to use this special method
    # Noteworthy how this allows for this method to be used without creating an object of the constructor-class.
    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True
    
    #### Properties section ####
    @property
    def pineapple_allowed(self):
        return False
    
    def meatballs_allowed(self):
        return False
    
    #### Setter/Getter section ####
    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password:")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

# Definition of list of ingredients
ingredients = ["cheese", "onions", "spam"]
# loop through all ingredients[] using the static method Pizza.validate_topping. If all are true, instantiate an object "pizza" of the class Pizza.
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

#########################################
# Properties                            #
#########################################

# Properties provide a way of customising access to instance attributes.
# They are created by putting the property decorator above a method. This means that when the instance attribute with the same name as the method is accessed,
# the method will be called instead. The property decorator is making the function a read-only ATTRIBUTE. This will now be called without parenthesis as it's an attribute.
# A common use of a property is to make an attribute read-only.

# We call the attribute / property and print its value
print("Is pineapple allowed on our pizza?", pizza.pineapple_allowed)
# To check if a no-@property attribute can indeed be changed we created a meatballs_allowed and print it.
# This print returns an object instead of a True/False statement.
# This seems because we don't call the method with a parenthesis. If we do, it works but pylint complains.
#  I guess that changed too with the Property decorator. The property returns False when using the same print statement.
print("Are meatballs permitted?", pizza.meatballs_allowed)
# We change the attribute to True, instead of false.
pizza.meatballs_allowed = True
# Print again, and indeed it worked.
print("Are our meatballs now permitted?", pizza.meatballs_allowed)
# We attempt to set the property attribute to false:
try:
    pizza.pineapple_allowed = True
except AttributeError:
    print ("Can't set attribute for a property, it's read-only")

# Properties can also be set by defining setter/getter functions.
# Normally you have:
# User --> Attribute
# User <-- Attribute
#
# Now with getter and setter we can have
# User --> setter with pw protection --> Attribute
# User <-- Getter <-- Attribute
#
# The setter function sets the corresponding property's value.
# The getter gets the value.
# To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.
# The same applies to defining getter functions.

# We have password protected the setting of the property pineapple_allowed. If we type the right password, we are allowed to change the read-only value.
# or at least that's what it did in the training software. In my code it does not.
print(pizza.pineapple_allowed)

