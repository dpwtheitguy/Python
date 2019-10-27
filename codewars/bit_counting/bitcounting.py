#/usr/bin/env python

'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''


def countBits(n):
  ''' Take in a int, make it a string with a binin there, yank out the leading characters and loop through counting up the 1s'''
  intcoutnof1s = 0
  strmybin = bin(n)
  strmybin = strmybin[2:]
  for char in strmybin:
      if char == '1':
          intcoutnof1s = intcoutnof1s + 1
  return intcoutnof1s 

# Call the test case provided
print(countBits(1234)) 