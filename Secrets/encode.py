# encode.py
import codecs

print('Enter the string you would like to encode?')
strusername = input()
strencoded = codecs.encode(strusername, 'rot_13')
print("your encoded string is: " + strencoded )

