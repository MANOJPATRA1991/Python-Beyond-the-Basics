# def tag(name, **kwargs):
  # print(name)
  # print(kwargs)
  # print(type(kwargs))

def tag(name, **attributes):
  # atributes has a type <class 'dict'>
  result = '<' + name
  for key, value in attributes.items():
    result += ' {k}="{v}"'.format(k=key, v=str(value))
  result += '>'
  return result