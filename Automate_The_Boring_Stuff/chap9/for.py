#/usr/bin/env python
# for.py
import os

skipfolders = ['chap8', 'chap10']

for foldername, subfolders, filenames in os.walk("C:\\Users\\danie\\OneDrive\\Documents\\Python\\automate_boring_stuff"):
    for subfolder in subfolders:
        if subfolder in skipfolders:
            continue
        print(subfolder)