#!/usr/bin/env python
# duplicatencoder.py 
'''
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
'''
from collections import Counter 


def duplicate_encode(word):
  newword = ""
  word = word.lower()
  count = Counter(word)
  for char in word:
    if 1 == count[char]:
      newword = newword + "("
    else:
      newword = newword + ")"
  return newword

# "Success"  =>  ")())())"
print(duplicate_encode('Success'))
