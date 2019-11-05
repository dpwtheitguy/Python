#/usr/bin/env python
# isograms.py

'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case

'''
import collections

def is_isogram(string):
   string = string.lower()
   c = collections.Counter(string)
   for char in c:
      if c[char] > 1:
          return 'False'

   return 'True' 


print(is_isogram('moOse')) 
