import socket

def resolve(host): 
  return socket.gethostbyname(host)

resolve
# => <function resolve at 0x7f12bc225ea0>

resolve('sixty-north.com')
# => '93.93.131.30'

"""
Callable instances
"""
from resolver import Resolver

resolve = Resolver()
resolve('sixty-north.com')
# => '93.93.131.30'

resolve.__call__('sixty-north.com')
# => '93.93.131.30'

resolve._cache
# => {'sixty-north.com': '93.93.131.30'}

resolve('pluralsight.com')
# => '54.201.247.181'

resolve._cache
# => {'sixty-north.com': '93.93.131.30', 'pluralsight.com': '54.201.247.181'}

resolve._cache
# => {'sixty-north.com': '93.93.131.30', 'pluralsight.com': '54.201.247.181'}

resolve.has_host('pluralsight.com')
# => True

resolve.clear()

resolve._cache
# => {}

"""
Class as callable
"""
def sequence_class(immutable): 
  # if immutable: 
  #   cls = tuple 
  # else: 
  #   cls = list 
  # return cls

  return tuple if immutable else list

seq = sequence_class(immutable=True)
t = seq("Timbuktu")
t
# => ('T', 'i', 'm', 'b', 'u', 'k', 't', 'u')

type(t)
# => <class 'tuple'>

seq = sequence_class(immutable=False)
# => ('T', 'i', 'm', 'b', 'u', 'k', 't', 'u')

t = seq('Timbuktu')
t
# => ['T', 'i', 'm', 'b', 'u', 'k', 't', 'u']

type(t)
# => <class 'list'>
   
"""
Lambda expressions
"""
scientists = [
  'Marie Curie', 
  'Albert Einstein', 
  'Niels Bohr',
  'Isaac Newton',
  'Dmitri Mendeleev',
  'Antonie Lavoisier',
  'Carl Linnaeus',
  'Alfred Wegener',
  'Charles Darwin'
]

sorted(scientists, key=lambda name: name.split()[-1])
# ['Niels Bohr', 'Marie Curie', 'Charles Darwin', 'Albert Einstein', 'Antonie Lavoisier', 'Carl Linnaeus', 'Dmitri Mendeleev', 'Isaac Newton', 'Alfred Wegener']

last_name = lambda name: name.split()[-1]
   
last_name
# => <function <lambda> at 0x7f05a29fbbf8>

last_name('Nikola Tesla')
# => 'Tesla'

# Functions are callable
callable(last_name)
# => True
   
# Lambda functions are callable
is_odd = lambda x: x%2 == 1
callable(is_odd)
# => True

# Classes are callable
callable(list) 
# => True

# Class methods are callable
callable(list.append)
# => True

# Class instances are callable
callable(resolve) 
# => True

"""
Extended function calls examples
"""
from geometry import hypervolume

print(hypervolume(2,4))
# => 8
print(hypervolume(2,4,6))
# => 48
print(hypervolume(2,4,6,8))
# => 384

from tag import tag

print(tag('img', src='monet.jpg', alt='Sunrise by Claude Monet', border=1))

# Extended call syntax
def print_args(arg1, arg2, *args):
  print(arg1)
  print(arg2)
  print(args)

t = (1,2,3)

print_args(*t)
# 1
# 2
# (3,)

def color(red, green, blue, **kwargs):
  print("r=", red)
  print("g=", green)
  print("b=", blue)
  print(kwargs)

k = {'red':21, 'green':68, 'blue':120, 'alpha':52}

color(**k)
# r= 21
# g= 68
# b= 120
# {'alpha': 52}

# dict uses extended keyword arguments technique
k = dict(red=21, green=68, blue=120, alpha=52)

"""
Forwarding Arguments
"""
def trace(f, *args, **kwargs):
  print("arg=", args)
  print("kwargs=", kwargs)
  result = f(*args, **kwargs)
  print("result=", result)
  return result

int("ff", base=16)
# => 255

trace(int, "ff", base=16)
# arg= ('ff',)
# kwargs= {'base': 16}
# result= 255

"""
zip using *args to accept arbitrary number of iterables
"""
sunday = [1,2,3,4,5]
monday = [11,22,33,44,55]
tuesday = [111,222,333,444,555]

daily = [sunday, monday, tuesday]

for item in zip(daily[0], daily[1], daily[2]):
  print(item)
# (1, 11, 111)
# (2, 22, 222)
# (3, 33, 333)
# (4, 44, 444)
# (5, 55, 555)

for item in zip(*daily):
  print(item)
# (1, 11, 111)
# (2, 22, 222)
# (3, 33, 333)
# (4, 44, 444)
# (5, 55, 555)

transposed = list(zip(*daily))
print(transposed)
# [(1, 11, 111), (2, 22, 222), (3, 33, 333), (4, 44, 444), (5, 55, 555)]