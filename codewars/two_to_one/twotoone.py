#!/usr/bin/env python

'''
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''


def longest(s1, s2):
    # your code
    strlongest = ""
    lstlongest = sorted(list(set(s1 + s2)))
    for i in lstlongest:
        strlongest = strlongest + i 
    return strlongest

# Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, a)) 