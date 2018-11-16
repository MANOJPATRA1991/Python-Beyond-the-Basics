from tracer import Trace
from map_reducer import count_words, combine_counts
from example_iterator import ExampleIterator, ExampleIterable
from alt_iterable import AlternateIterable
import sensor

"""
Comprehensions:

short-hand syntax for creating collections and iterable objects
"""
l = [i*2 for i in range(10)]
type(l)
# => <class 'list'>

d = {i: i*2 for i in range(10)}
type(d)
# => <class 'dict'>

s = {i for i in range(10)}
type(s)
# => <class 'set'>

l
# => [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

d
# => {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

s
# => {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

g = (i for i in range(10))
type(g)
# => <class 'generator'>

g
# => <generator object <genexpr> at 0x7fb927885a40>

# Second for loop is nested inside the first for loop
[(x, y) for x in range(5) for y in range(3)]
# => [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)]

"""
Above comprehension is equivalent to:
"""
points = []

for x in range(5): 
  for y in range(3): 
    points.append((x, y))
points
# => [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)]

"""
Benefits of comprehensions:

1. Container populated "atomically"
2. Allows Python to omptimize creation
3. More readable
"""
# later clauses can refer to variables bound in the earlier clauses
values = [x / (x - y) 
          for x in range(100) 
          if x > 50 
          for y in range(100) 
          if x - y != 0]

"""
Above comprehension is equivalent to:
"""
values = []
for x in range(100):
  if x > 50:
    for y in range(100):
      if x - y != 0:
        values.append(x / (x - y))

[(x,y) for x in range(10) for y in range(x)]

"""
Above comprehension is equivalent to:
"""
results = []
for x in range(10):
  for y in range(x):
    results.append((x,y))

"""
Comprehensions can be nested inside other comprehensions
=> Each element in the collection produced by a comprehension can itself be a comprehension
"""
vals = [[y*3 for y in range(x)] for x in range(10)]

"""
Above comprehension is equivalent to:
"""
outer = []
for x in range(10):
  inner = []
  for y in range(x):
    inner.append(y*3)
  outer.append(inner)

print(outer)
# [[], [0], [0, 3], [0, 3, 6], [0, 3, 6, 9], [0, 3, 6, 9, 12], [0, 3, 6, 9, 12, 15], [0, 3, 6, 9, 12, 15, 18], [0, 3, 6, 9, 12, 15, 18, 21], [0, 3, 6, 9, 12, 15, 18, 21, 24]]

{x*y for x in range(10) for y in range(10)}
# => {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42, 45, 48, 49, 54, 56, 63, 64, 72, 81}
   
g = ((x,y) for x in range(10) for y in range(x))

type(g)   
# => <class 'generator'>

list(g)
# => [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (4, 3), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)]

"""
map() : 
1. apply a function to every element in a sequence, providing a new sequence

2. map can accept any number of input sequences

3. The number of input sequences must match the number of function arguments
"""
# Does lazy evaluation, i.e., it does not produce any output unless needed
map(ord, 'The quick brown fox') # Produces an iterator object
# => <map object at 0x7fd0c30a5f98>

list(map(ord, 'The quick brown fox'))   
# => [84, 104, 101, 32, 113, 117, 105, 99, 107, 32, 98, 114, 111, 119, 110, 32, 102, 111, 120]

result = map(Trace()(ord), 'The quick brown fox')

print(result) # <map object at 0x7eff45f47828>

print(next(result)) # we are manually running the function on the map object returned by the map
# Calling <built-in function ord>
# 84

result = list(map(Trace()(ord), 'The quick brown fox'))

print(result)

"""
map(f, a,b,c) => where a,b,c are collections => map takes one element from each sequence at a time and passes them as arguments to the function f in order, to produce the next output value of the map

map will terminate as soon as any of the input sequences is terminated
"""
sizes = ['small', 'medium', 'large']
colors = ['lavender', 'teal', 'burnt orange']
animals = ['koala', 'platypus', 'salamander']

def combine(size, color, animal):
  return '{} {} {}'.format(size, color, animal)

res = list(map(combine, sizes, colors, animals))
print(res)
# ['small lavender koala', 'medium teal platypus', 'large burnt orange salamander']

import itertools

def combine(quantity, size, color, animal):
  return '{} x {} {} {}'.format(quantity, size, color, animal)

res = list(map(combine, itertools.count(), sizes, colors, animals))

print(res)
# ['0 x small lavender koala', '1 x medium teal platypus', '2 x large burnt orange salamander']

"""
map() vs. comprehensions
"""
[str(i) for i in range(5)]
# => ['0', '1', '2', '3', '4']

"""
is equivalent to
"""

list(map(str, range(5)))   
# => ['0', '1', '2', '3', '4']

i = (str(i) for i in range(5))
type(i) 
# => <class 'generator'>
list(i)
# => ['0', '1', '2', '3', '4']
"""
Compare the above and below code snippets
"""
i = map(str, range(5))
type(i)
# => <class 'map'>
list(i)
# => ['0', '1', '2', '3', '4']

"""
filter() :
1. apply a function to each element in a sequence, constructing a new sequence with the elements for which the function returns True

2. Produces results lazily like map

3. Unlike map, only accepts a single input sequence and the function it takes must only accept a single argument

4. Passing None as the first argument to filter() instead of a function or lambda expression will remove elements which evaluate to False

NOTE: In Python 2, map() and filter() are eagerly evaluated and return list objects
"""
positives = filter(lambda x: x>0, [1,-5,0,6,-2,8])
positives
# => <filter object at 0x7f86e3f44390>
list(positives)
# => [1, 6, 8]

# 4.
trues = filter(None, [0,1,False,True,[],[1,2,3],'','hello'])
print(list(trues)) # [1, True, [1, 2, 3], 'hello']

"""
functools.reduce() : 

** Repeatedly apply a function to the elements of a sequence, reducing them to a single value **

1. repeatedly apply a function of two arguments to an interim accumulator value and each element of the series in turn updating or accumulating the interim value at each stage with the result of the called function. 

** The callable function takes two arguments -- the accumulated result so far and the next element

2. The initial value of the accumulator can either be the first element of the sequence or an optional value we supply.

3. Ultimately, the final value of the accumulator is returned, thereby reducing the sequence down to a single value
"""

from functools import reduce
import operator
print(reduce(operator.add, [1,2,3,4,5])) # 15

"""
The above reduce() call is equivalent to
"""
numbers = [1,2,3,4,5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
  accumulator = operator.add(accumulator, item)

print(accumulator) # 15

def mul(x,y):
  print('mul {} {}'.format(x,y))
  return x*y

print(reduce(mul, range(1, 10))) 
# OUTPUT:
# mul 1 2
# mul 2 3
# mul 6 4
# mul 24 5
# mul 120 6
# mul 720 7
# mul 5040 8
# mul 40320 9
# 362880

# reduce(mul, []) => Passing an empty sequence to reduce raises a TypeError
reduce(mul, [1]) # => Passing one element will simply return that element without ever calling the reducer function

# optional initial value to reduce()
values = [1,2,3]
print(reduce(operator.add, values, 0)) # 6

values = []
print(reduce(operator.add, values, 0)) # 0

"""
map-reduce
"""
count = count_words('It was the best of times, it was the worst of times.')

print(count)
# {'it': 2, 'was': 2, 'the': 2, 'best': 1, 'of': 2, 'times': 2, 'worst': 1}

documents = [
  'It was the best of times, it was the worst of times.',
  'I went to the woods because I wished to live deliberately, to front only ...',
  'Friends, Romans, countrymen, lend me your ears; I come to bury Caesar, not to ...',
  'I do not like green eggs and ham. I do not like them, Sam-I-Am.',
]

counts = map(count_words, documents)
# print(list(counts))
# [{'it': 2, 'was': 2, 'the': 2, 'best': 1, 'of': 2, 'times': 2, 'worst': 1}, {'i': 2, 'went': 1, 'to': 3, 'the': 1, 'woods': 1, 'because': 1, 'wished': 1, 'live': 1, 'deliberately': 1, 'front': 1, 'only': 1}, {'friends': 1, 'romans': 1, 'countrymen': 1, 'lend': 1, 'me': 1, 'your': 1, 'ears': 1, 'i': 1, 'come': 1, 'to': 2, 'bury': 1, 'caesar': 1, 'not': 1}, {'i': 3, 'do': 2, 'not': 2, 'like': 2, 'green': 1, 'eggs': 1, 'and': 1, 'ham': 1, 'them': 1, 'sam': 1, 'am': 1}]

total_counts = reduce(combine_counts, counts)
print(total_counts)
# {'it': 2, 'was': 2, 'the': 3, 'best': 1, 'of': 2, 'times': 2, 'worst': 1, 'i': 6, 'went': 1, 'to': 5, 'woods': 1, 'because': 1, 'wished': 1, 'live': 1, 'deliberately': 1, 'front': 1, 'only': 1, 'friends': 1, 'romans': 1, 'countrymen': 1, 'lend': 1, 'me': 1, 'your': 1, 'ears': 1, 'come': 1, 'bury': 1, 'caesar': 1, 'not': 3, 'do': 2, 'like': 2, 'green': 1, 'eggs': 1, 'and': 1, 'ham': 1, 'them': 1, 'sam': 1, 'am': 1}

"""
Python iteration:

1. iter() : create an iterator
2. next() : get next element in sequence

StopIteration : signal the end of the sequence

iterable : an object which implements the __iter__() method
iterator : an object which implements the iterable protocol

All iterators must implement __iter__()
Iterators need to implement the __next__() method 

__iter__() should return an iterator for the iterable object

__next__() method returns the next value in whatever sequence the iterator represents or raise the StopIteration exception when the sequence is exhausted
"""
# i = ExampleIterator()
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# 2
# 3
# Traceback (most recent call last):
#   File "main.py", line 314, in <module>
#     print(next(i))
#   File "/home/runner/example_iterator.py", line 11, in __next__
#     raise StopIteration
# StopIteration

# for i in ExampleIterator():
#   print(i)

"""
Iterator and Iterable protocols working together
"""
for i in ExampleIterable():
  print(i)
# 1
# 2
# 3

print([i*3 for i in ExampleIterable()])
# [3, 6, 9]

"""
The alternative iterable protocol works with any object that supports consecutive integer indexing via __getitem__(index). When index out of range, it must raise IndexError exception.
"""
print([i for i in AlternateIterable()])
# [1, 2, 3]

"""
Using extended iter with objects that do not support the iterable protocol

iter(callable, sentinel) :
--------------------------
Arguments:
callable : callable object that takes zero arguments
sentinel : iteration stops when callable produces this 
value

Return:
An iterator which produces values by repeatedly calling the callable argument

USe of this iter() : To create infinite sequences from normal existing functions
"""
# import datetime
# j = iter(datetime.datetime.now, None)
# print(next(j))
# print(next(i))
# print(next(i))

# Read from a file until we reach a line containing just the string 'END'
with open('ending_file.txt', 'rt') as f:
  for line in iter(lambda: f.readline().strip(), 'END'):
    print(line)