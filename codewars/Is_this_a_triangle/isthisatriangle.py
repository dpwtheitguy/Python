#!/usr/bin/env python

'''
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
'''
import math 

def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
       s = ((a + b + c) / 2)
       temp = (s - a)*(s - b)*(s - c)
       temp = temp*s
       if temp > 0:
          area = math.sqrt(temp)
          return True
       else:
           return False
    else:
        return False


print(is_triangle(-1,2,3))
# 1, 2, 3