class Base:
  def __init__(self):
    print('Base initializer')

  def f(self):
    print('Base.f()') 

class Sub(Base):
  def __init__(self):
    super().__init__()
    print('Sub initializer')
  # Overriding base class's f() method
  def f(self):
    print('Sub.f()')