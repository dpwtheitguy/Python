#/usr/bin/env python
#stringsstuff.py

import pyperclip

print(' '.join(['hello','world']))

print('hello'.rjust(20)) 
print('hello world'.rjust(20))

print('hello'.rjust(20, "*")) 
print('hello world'.rjust(20, "-"))


# pyperclip.copy('hello world')

print(pyperclip.paste() )