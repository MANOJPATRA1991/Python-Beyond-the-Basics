# Summary

## Class Attributes vs. Static Attributes
* EXPLICIT IS BETTER THAN IMPLICIT.

### Class Attributes

	* Class attributes are defined on the class outside the __init__ function.

	* Classes don't introduce new scopes. Class attributes are referred by their class names.

	* There are only four scopes referred to as LEGB: Local, Enclosing Functions, Global and Built-in.

	* Class attributes are attributes that are available across all instances of the class.

	* Class attributes can be accessed directly from the class as well as from the instances of the class.

	* But attempting to assign to a class attribute with the self reference (example: self.attr = 23), will create a new instance attribute instead and the class attribute will remain unmodified.

### Static methods

	* Static methods are defined on the class object.

	* To declare a method static, use the @staticmethod decorator.

	* We can also define something called a class method with the @classmethod decorator which takes cls as its first argument, which is simply a reference to the class object.

	* Implementation details of a class method (functions inside class) should always start with an _

	* Static methods in Python have no knowledge of the class within which they are defined.

### Choosing between class method and static method

	* We should use @classmethod when we need to access the class object in order to use class methods or the constructor.

	* Static methods are used when no access to class or instance objects are required.
	  They are most likely an implementation detail of the class.
	  The @staticmethod decorator merely facilitates a logical organisation of code allowing us to put inside classes what would otherwise be free functions.

	* Static method names should start with an _

	* Named Constructors or Factory Functions: Functions within class which construct objects with certain configurations.

	* Static methods and Inheritance: Static methods in Python can be overridden in sub-classes (Inheritance). For polymorphic dispatch of static method invocation, call through the self instance.

	* Class methods and Inheritance: Class methods behave polymorphically as a distinguished feature of Python

	* To extend super class constructor inside derived class's constructor, use super(). __init__()

	* Private properties of a class are named starting with an _

	* The @property decorator can be used to transform getter methods so that they can be called as if they were attributes.


Template Design Pattern:
https://sourcemaking.com/design_patterns/template_method/python/1
