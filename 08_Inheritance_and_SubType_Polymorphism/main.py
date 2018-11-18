"""
Single inheritance
------------------
class SubClass(BaseClass) -> SubClass will have all of the methods of BaseClass and SubClass will be able to override these methods if it wants to. SubClass can do everything that BaseClass can do and it can also modify that behavior.

To make sure the full object is initialized, subclass initializer will call the baseclass initializer

If subclass initializer is not defined, then the baseclass initializer will be called when an instance of subclass is created.
"""
from base import Base, Sub
b = Base()
# Base initializer

b.f()
# Base.f()

s = Sub()
# Base initializer if __init__ is not available for Sub else 
# Sub initializer

# The following output is when we call super class's __init__ with super().__init__()
# Base initializer
# Sub initializer


s.f()
# Sub.f()

"""
Other languages automatically call base class initializers. But Python treats __init__() like any other method. Base class __init__() is not called if overridden. To call base class's __init__() along with subclass's __init__() use super()
"""
from sorted_list import SortedList
sl = SortedList([4,3,2,1])
print(sl) # SortedList([1, 2, 3, 4])
print(len(sl)) # 4
sl.add(-42)
print(sl) # SortedList([-42, 1, 2, 3, 4])

"""
isinstance() --> determinses if an object is of a specified type
            --> used for run time type checking
"""
# Examples
isinstance(3, int)
# => True
x = []
isinstance(x, (float, dict, list))
# => True

"""
CHECKING FOR SPECIFIC TYPES IS BAD DESIGN IN PYTHON
"""

from sorted_list import IntList, SimpleList
il = IntList([1,2,3,4])
il.add(19) # IntList([1, 2, 3, 4, 19])
print(il)
# il.add('5')
# print(il) # TypeError: IntList only supports integer values.

"""
issubclass() : determines if one type is a subclass of another
--> operates on types only rather than on instances
--> used to determine if one class is a subclass of another
"""
print(issubclass(SortedList, SimpleList)) # True
print(issubclass(SortedList, IntList)) # False

# EXAMPLE
class MyInt(int): pass
class MyVerySpecialInt(MyInt): pass
print(issubclass(MyVerySpecialInt, int)) # True

"""
multiple inheritance
--------------------
defining a class with more than one base class

Python has a simple and understandable system for multiple inheritance as compared to other languages that support multiple inheritance such as c++ in cases such as what if more than one base classes define the same method. Java does not support multiple inheritance

class SubClass(Base1, Base2, ...)

1. Subclasses inherit methods of all bases

2. Without conflict, names resolve in the obvious way

3. Method Resolution Order(MRO) determines name lookup in all cases such as method name duplication
"""
from sorted_list import SortedIntList
sil = SortedIntList([42,23,2])
print(sil) # SortedIntList([2, 23, 42])
# print(SortedIntList([3,2,'1']))
# TypeError: IntList only supports integer values.
sil.add(-1234)
print(sil) # SortedIntList([-1234, 2, 23, 42])
# sil.add('hi')
# TypeError: IntList only supports integer values.

"""
If a class has multiple base classes but no initializer defined, then only the initializer of the first base class is automatically called when an instance of that class is created
"""
class Base1:
  def __init__(self):
    print('Base1.__init__')

class Base2:
  def __init__(self):
    print('Base2.__init__')

class Sub(Base1, Base2):
  pass

s = Sub() # Base1.__init__ => Only Base1 __init__() is called

"""
All class objects have a __bases__ property which is a tuple of base classes the class inherits from
"""
print(SortedIntList.__bases__)
# (<class 'sorted_list.IntList'>, <class 'sorted_list.SortedList'>)

"""
MRO
---
Defines the ordering of a class's inheritance graph used to determine which implementation to use when a method is invoked

special member __mro__ can be used to access a class's mro in the form of a tuple
mro() can be used to access a class's mro in the form of a list

C3 : algorithm for calculating MRO in Python
--------------------------------------------
It ensures:

1. Subclasses come before base classes

2. Base class order from class definition is preserved

3. First two qualities are preserved no matter where we start in the inheritnce graph
"""
print(SortedIntList.__mro__)
# (<class 'sorted_list.SortedIntList'>, <class 'sorted_list.IntList'>, <class 'sorted_list.SortedList'>, <class 'sorted_list.SimpleList'>, <class 'object'>) 

print(SortedIntList.mro())
# [<class 'sorted_list.SortedIntList'>, <class 'sorted_list.IntList'>, <class 'sorted_list.SortedList'>, <class 'sorted_list.SimpleList'>, <class 'object'>]

from diamond import *

print(D.mro())
# [<class 'diamond.D'>, <class 'diamond.B'>, <class 'diamond.C'>, <class 'diamond.A'>, <class 'object'>]

"""
object is the ultimate base class of every class in Python
"""
d = D()
print(d.func())


"""
Given a method resolution order(MRO) and a class C, super() gives you an object which resolves methods using only the part of the MRO which comes after C

super() returns a proxy object which routes method calls. Proxies are of two types:

1. Bound proxy -- bound to a specific class or instance
    |
    |__ instance-bound
    |    |
    |    |
    |    |
    |    |                 instance of first argument or any class derived from it
    |    |                    /\
    |    |                   /||\
    |    |                    ||
    |    super(class, instance-of-class)
    |           ||
    |          \||/
    |           \/
    |         class object
    |    
    |   i> Finds the MRO for the type of the second argument
    |   
    |   ii> Finds the location of the first argument in the MRO
    |
    |   iii> Uses everything after that for resolving methods
    |   NOTE: Since, the proxy is bound to an instance, we can call the methods after they are bound
    |
    |__ class-bound
        |                     subclass of first argument
        |                        /\
        |                       /||\
        |                        ||
        |__super(base-class, derived-class)
                     ||
                    \||/
                     \/
                class object     

            i> Python finds MRO for derived-class

            ii> It then finds base-class in that MRO
            
            iii> It takes everything after base-class in the MRO and finds the first class in that sequence with a matching method name           

2. Unbound proxy -- not bound to a class or instance -- primarily used for implementing other Python features
"""
print(super(SortedList, SortedIntList).add)
# <function SimpleList.add at 0x7f1c2d7428c8>

# print(super(SortedList, SortedIntList).add(1)) # won't work
print(super(SortedIntList, SortedIntList)._validate(5)) # will work only with static methods

# super(int, IntList) # throws Error when first argument is not the base class of the second argument

from sorted_list import *
from pprint import pprint as pp
pp(SortedIntList.mro())
# [<class 'sorted_list.SortedIntList'>,
#  <class 'sorted_list.IntList'>,
#  <class 'sorted_list.SortedList'>,
#  <class 'sorted_list.SimpleList'>,
#  <class 'object'>]

sil = SortedIntList([5,15,10])
print(sil)
# SortedIntList([5, 10, 15])
print(super(SortedList, sil))
# <super: <class 'SortedList'>, <SortedIntList object>> 

super(SortedList, sil).add(6) # resolves add() to SimpleList's add() from the MRO

print(sil)
# SortedIntList([5, 10, 15, 6]) # Design broken

"""
calling an instance method => super(class-of-method, self)
calling a class method => super(class-of-method, class)

class-of-method is always the first argument to super() and the first argument to the method which can be either self/class is the second argument to super()
"""

"""
object
------

- the core of the Python object model
- object is the ultimate base class of every class
- object is automatically added as a base class
"""
class NoBaseClass: pass
print(NoBaseClass.__bases__) # (<class 'object'>,)
print(dir(object))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

"""
Summary
-------
Unlike C++ and Java, the type name of an object does not determine if they can be used in a given context. Rather, Python uses duck typing, where an object's fitness for a use is only determined at the time it's actually used and exceptions are raised if an object doen not have necessary attributes to fulfil a request.

Functions are defined without specifying type names on their arguments, and we can pass objects of any type to any function. Likewise, we can call any method we want with any object and Python won't complain until run time. --> This gives an idea of how inheritance in Python is different from other languages.pass

TYPE MANAGEMENT IS TIRING.

Inheritance in Python is based used for implementation rather than type management. IT is a convenient way to reuse code much more than it is a way to construct type hierarchies.
"""