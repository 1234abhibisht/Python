# OOPS (Object Oriented Programming) is a way of writing program by combining data and behaviour using 
# objects and classes.
# -> Focuses on real world entities.
# -> data and method are combined
# -> It increases reusability, security, scalability of our program


# The alternative of OOPs is Functional Programming(FP), where we use functions in our program,
# which we were doing till now
# but in real world systems, large databases Functional Programming is not suitable.
# In real world systems we use OOPs


# Feature                     OOPS              Functional Programming

# -> Core unit                object             functions
# -> Data handling            easy               difficult
# -> Real world modelling     easy               difficult 
# -> Application              large projects     some small logic based take(such as dsa etc)


# OOPs bind data and behaviour together, while function keeps them seperate

# Example we want to create a student record system
# -> we use functions, then we have to create different functions and call them again and again
# -> In such case use can use OOPs concept


# Class -> We can define class as a blueprint of an object
#       -> class defines the data and behaviour of the object
#       -> so we can say, class is an blueprint that binds variable and function
#   We can understand this like, we have a blueprint of a builiding, the blueprint contains number
#   of apartments, rooms in each apartment etc, so this blueprint is the class 

#   Say, class is just a plan that how our object will look like



# Class contains, variables -> also known as attributes
#                 functions -> also known as methods



# objects -> As we said, class is a bluprint of a real entity, but object is that real entitiy


# Why we need objects ?
# -> object allows multiple entities of a class
# -> object holds real data


# Class variable and Instance variable

# Class variable -> Shared by all objects
#                -> defines directly inside the class and outside methods(functions)

# Instance variable -> Unique for each object
#                   -> defined inside __inti__ using self



# self -> self refers to current object
#      -> self is used to access variables and methods of an object


# Methods

# Methods are functions defined within a class that describe the behaviors of its objects. 
# They allow objects to perform actions and interact with their data. Unlike regular functions, methods are called on objects and often use the self parameter to access instance-specific data.

# Types of Methods

# Instance methods: Most common type of method in Python classes. 
# They operate on individual objects and have access to instance attributes through the self parameter.

# Class methods: defined with the @classmethod decorator and take cls as their first parameter instead of self. 
# They can access and modify class-level data shared by all instances.

# Static methods: defined with the @staticmethod decorator and do not take self or cls as their first parameter. 
# They behave like regular functions but belong to the class's namespace.


# attribute -> variable stored in an object


# instance -> single unique object created from a class


# constructor -> __init__()  way to represent constructor
#             -> when we create a new object, then we can initialize its data using constructor
#             -> It is called automatically when object is created

# if we declare variable in a class without constructor, that variable will work as class variable,
# and if we declare variable inside constructor / def __inti__() : /, that variable will work as instance variable


# object creation flow
# -> first memeory is created for that object
# -> them constructor is called automatially as object is created
# -> data in input in object\
    
    
# four pillars of oops
# -> Encapsulation - data protection
# -> Abstraction - hiding complixity
# -> Inheritance - code reusable
# -> Polymorphism - flexibility

# These pillars makes data secure, easy to maintain, resusable, scalable


# Built-in Attributes
# In Python, every class automatically contains some built-in attributes that provide useful information about the class.
# These attributes help in introspection (examining class properties at runtime).
# Purpose of Built-in Attributes

# To inspect class details dynamically.
# Useful in debugging and development.
# Helps understand class structure and inheritance.
# Attribute Description
# __name __ : Name of the class.
# __module __ : Name of the module in which class is defined.
# __doc __ : Documentation string (docstring) of the class.
# __bases __ : Tuple containing base (parent) classes.
# __dict __ : Dictionary containing class namespace (attributes & methods).

# Abstract Class
# An abstract class is a class that cannot be instantiated directly.
# It is used as a blueprint for other classes.

# An abstract class can contain:

# Abstract methods → methods declared but not implemented
# Normal methods → methods with implementation

# Why use Abstract Class?
# To define a common structure for child classes
# To force subclasses to implement required methods
# To improve code consistency and design
# Key Points:
# Abstract classes are created using the ABC class from the abc module.
# Abstract methods are created using the @abstractmethod decorator.
# A child class must implement all abstract methods.
# Real-world Analogy:
# Think of a vehicle blueprint:

# A blueprint tells what features every vehicle should have (start, stop).
# But the exact implementation differs for a car, bike, or truck.
# Similarly, an abstract class defines what methods should exist, while child classes decide how to implement them.


# Garbage Collection
# Process of automatically freeing memory by deleting objects that are no longer in use.
# Why Garbage Collection is Needed?
# Efficient memory management.
# Prevents memory leaks.
# Automatically removes unused objects.

# Memory management is automatic in Python.
# Most of the time, GC works in the background.
# Important Functions:

# gc.collect() → Forces garbage collection
# gc.get_count() → Returns GC statistics
# gc.disable() / gc.enable() → Control GC
