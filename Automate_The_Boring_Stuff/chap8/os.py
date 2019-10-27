#/usr/bin/env python

import os
import shelve
print("Chapter 8 ")

# Printing a path
print(os.path.join('C:\\','Users', 'danie', 'Downloads'))

# for loop of files
lstFiles = ['file01.txt', 'file02.txt', 'file03.txt']

for strFile in lstFiles:
    print(os.path.join('C:\\','Users', 'danie', 'Downloads', strFile))

# Current Working Directory
print(os.getcwd())
os.chdir('C:\\Windows\\System32')
print(os.getcwd())

# make some directories
#os.makedirs('C:\\temp\\deleteme')

# Relative 
# I am in the seond parameter folder, how do I get tgo the other one with a CD
print(os.path.relpath("C:\\", "C:\\Windows"))
print(os.path.relpath("C:\\Windows", "C:\\"))

# Playing with Splitting a path
strCalcPath = 'C:\\Windows\\System32\\calc.exe'
print(strCalcPath.split(os.path.sep))
print(os.path.sep)
print(strCalcPath.split('\\'))

# Get File Size
print("get size")
print(os.path.getsize(strCalcPath))
print(os.listdir('C:\\Windows'))

# do some looping around files
size = 0
for file in os.listdir('C:\\Windows'):
    size = os.path.getsize(os.path.join('C:\\Windows',file)) + size
print(size)

# File Stuff
#strFolder = 'C:\\Users\\danie\\OneDrive\\Documents\\Python\\automate_boring_stuff\\chap8\\example.txt'
#myFile = open(strFolder)
#print(myFile.read())
#myFile.close()

# Shelves - output
print(os.getcwd())
os.chdir('C:\\Users\\danie\\OneDrive\\Documents\\Python\\automate_boring_stuff\\chap8')
print(os.getcwd())
shelfFile = shelve.open('mydata')
cats = ['Cat0','Cat1','cat2']
shelfFile['cats'] = cats 
shelfFile.close() 

# shelves - input
shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])

# shutil
import shutil 
