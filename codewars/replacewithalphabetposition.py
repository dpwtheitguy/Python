#!/usr/bin/env python

'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
 
Notes:
 ord('a') - 96
'''

def alphabet_position(text):
    text = text.lower()
    print(text)
    strFinal = ""
    for char in text:
        if char.isalpha():
            strFinal = strFinal + str(ord(char) - 96) + " "
    strFinal = strFinal[:-1]
    return strFinal

print(alphabet_position("The narwhal bacons at midnight."))

