# def hypervolume(*args):
#   print(args)
#   print(type(args))

"""
Raises StopIteration when no arguments supplied
"""
# def hypervolume(*lengths):
#   i = iter(lengths)
#   v = next(i)
#   for length in i:
#     v *= length
#   return v

# Simpler and easier to understand
def hypervolume(length, *lengths):
  # lengths has a type <class 'tuple'>
  v = length
  for item in lengths:
    v *= item
  return v
