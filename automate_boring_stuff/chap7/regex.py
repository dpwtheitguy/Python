#/usr/bin/env python
# regex.py
import re


# single return
rePhoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = rePhoneNumber.search('My number is 415-555-4242')
print('Phone Number Found ' + mo.group())
print(type(mo))

# multiple capture groups
rePhoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = rePhoneNumber.search('My number is 415-555-4242')
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))

# findall method
print("Finall Method time!")
rePhoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
lstNumbers = rePhoneNumber.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(type(lstNumbers))
print(lstNumbers[1])

# findall method
print("Finall Method time with parathen!")
rePhoneNumber = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
lstNumbers = rePhoneNumber.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(type(lstNumbers))
print(lstNumbers)
print(lstNumbers[1][1])

# Basically sed
rePhoneNumber = re.compile(r'Daniel')
strSomeString = "hello there"
print(rePhoneNumber.sub("TEST", "MystringDanieltesthello"))
werfwerfwe