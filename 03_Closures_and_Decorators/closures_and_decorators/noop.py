#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

def noop(f):
  @functools.wraps(f)
  def noop_wrapper():
      # noop_wrapper.__doc__ = f.__doc__
      # noop_wrapper.__name__ = f.__name__
      return f()
  return noop_wrapper


@noop
def hello_noop():
  """Print a well-known message."""
  print("Hello, world!")