#!/usr/bin/env python
# -*- coding: utf-8 -*-

store = []

# Sort a list of strings by the last letter
def sort_by_last_letter(strings):
  # Return last letter of a string
  def last_letter(s):
      return s[-1]
  store.append(last_letter)
  print(last_letter)
  return sorted(strings, key=last_letter)