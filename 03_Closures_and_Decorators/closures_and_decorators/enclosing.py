#!/usr/bin/env python
# -*- coding: utf-8 -*-

message = 'global'

def enclosing():
  message = 'enclosing'

  def local():
    # We get a SyntaxError if the name doesn't exist when using nonlocal keyword
    # nonlocal no_such_name
    nonlocal message
    message = 'local'

  print('enclosing message:', message)
  local()
  print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)