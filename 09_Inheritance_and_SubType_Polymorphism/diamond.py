class A:
  def func(self):
    return 'A.func'

class B(A):
  def func(self):
    return 'B.func'

class C(A):
  def func(self):
    return 'C.func'

class D(B, C):
  pass

# class D(B, A, C):
#   pass
# Cannot create a consistent method resolution order (MRO) for bases A, C