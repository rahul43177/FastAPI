"""
OOPS -> Object Oriented Programming


What is Object Oriented Programming? 
Object Oriented Programming (OOP) is a programming paradigm that organizes code into objects that contain data and code.
It's based on the concept of objects that can contain:

- Data in the form of attributes/properties 
- Code in the form of methods/functions

Key concepts of OOP:

1. Classes - Blueprint for creating objects
2. Objects - Instances of a class
3. Encapsulation - Bundling data and methods that work on that data within a single unit
4. Inheritance - Creating new classes that are built upon existing classes
5. Polymorphism - Objects can take multiple forms
6. Abstraction - Hiding complex implementation details and showing only necessary features

Example:
class Car:
    def __init__(self, make, model):
        self.make = make    # Attribute
        self.model = model  # Attribute
    
    def display_info(self):  # Method
        return f"{self.make} {self.model}"

# Creating object
my_car = Car("Toyota", "Camry")



Objects -> Trees , Houses , Dog , Cat , Car , Bike , etc.
There are two ways to define them -> 
1. Behavior 
2. State 

Dog -> Behavior -> Bark , Run , Eat , Sleep , etc.
State -> Color , Breed , Name , Age , etc.

Dog -> Barking , Eating , Sleeping , Running , etc.
State -> 4 legs , 2 eyes , 1 nose , 1 mouth , 1 tail , 5 years old , etc.





"""

from dog_class import * 
#Dogs with primitive data types
#This is not how we do it in OOP 
legs : int = 4 
ears : int = 2 
type : str = "Golden Retriever"
name : str = "Max" 
color : str = "Brown "


dog = Dog()

"""
4 pillars of OOP -> Encapsulation , Inheritance , Polymorphism , Abstraction
1. Encapsulation -> 
2. Inheritance -> 
3. Polymorphism -> 
4. Abstraction -> 

Encapsulation -> Bundling data and methods that operate on that data within a single unit (class).
It restricts direct access to some object's components to prevent unintended interference.
Example: Making attributes private and accessing them through getter/setter methods.

Inheritance -> Allows a class to inherit attributes and methods from another class.
The class that inherits is called child/derived class, and the class being inherited from is parent/base class.
Example: class Dog(Animal) inherits from Animal class.

Polymorphism -> Ability of different classes to be treated as instances of the same class through inheritance.
It allows performing a single action in different ways.
Example: Different animals making different sounds using the same method name sound().

Abstraction -> Hiding complex implementation details and showing only necessary features of an object.
It reduces complexity by hiding unnecessary details.
Example: Using abstract classes and interfaces to define a common interface for a group of related classes.

"""

