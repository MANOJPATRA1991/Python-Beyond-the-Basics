from closures_and_decorators import *

sort_by_last_letter(['hello', 'from', 'a', 'local', 'function'])
# => ['a', 'local', 'from', 'function', 'hello']

sort_by_last_letter(['hello', 'from', 'a', 'local', 'function'])
# => ['a', 'local', 'from', 'function', 'hello']

sort_by_last_letter(['hello', 'from', 'a', 'local', 
'function'])
# => ['a', 'local', 'from', 'function', 'hello']

# OUTPUT FROM ABOVE CODE
# <function sort_by_last_letter.<locals>.last_letter at 0x7f053afc6e18>
# <function sort_by_last_letter.<locals>.last_letter at 0x7f053ac06598>
# <function sort_by_last_letter.<locals>.last_letter at 0x7f053ac06730>

def enclosing():
  x = 'local_func'
  def local_func():
    print(x)
  return local_func

"""
In the following example, we are returning a function from an enclosing function which we then bind to a named variable and finally call like any other function.
"""
lf = enclosing()
lf()

lf.__closure__
# => (<cell at 0x7f07cb2551c8: str object at 0x7f07caeb1ef0>,)

"""
Function Factory
"""
square = raise_to(2)

square(3) # => 9
square(8) # => 64

cube = raise_to(3)

cube(5) # => 125

enclosing()
# OUTPUT
# global message: global
# enclosing message: enclosing
# enclosing message: local
# global message: global

"""
Normal decorator example
"""
t = make_timer()

print(t()) # => None

print(t()) # => 1.1920928955078125e-05

t1 = make_timer()

print(t1()) # None

# t1 and t  are independent of each other

print(northern_city()) # 'Troms\xf8'

"""
Class decorator example
"""
hello('Manoj')
hello('Nick')
# hello.f('Nick')
print(hello.f, hello.count)
# <function hello at 0x7f09f94a3a60> 2

l = [1,2,3]
print(rotate_list(l))
# Calling <function rotate_list at 0x7f09f94a3bf8>
# [2, 3, 1]

"""
Instance decorator example
"""
im = IslandMaker(' Island')
print(im.make_island('Python'))

# Calling <function IslandMaker.make_island at 0x7fc7b49f1378>
# Python Island

"""
Using decorators for validation purposes
"""
print(create_list('a', 3))

print(create_list(123, -6))