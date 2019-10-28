#!/usr/bin/env python
# uniqueinorder.py

'''
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''

def unique_in_order(strDuplicates):
  lstFinal = []
  charLast = ""
  charCurrent =""
  for charCurrent in strDuplicates:
      print("last is" + charLast)
      print("current is" + charCurrent)
      if charCurrent != charLast:
          lstFinal.append(charCurrent)
          charLast = charCurrent
      else:
          charLast = charCurrent
  return lstFinal




print(unique_in_order('AAAABBBCCDAABBB'))