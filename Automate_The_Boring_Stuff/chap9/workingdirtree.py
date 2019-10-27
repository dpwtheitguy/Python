#/usr/bin/env python
# working dirtree.py

import os

for folderName, subFolders, filenames in os.walk('C:\\Users\\danie\\OneDrive\\Documents\\Python'):
    print('The Current Folder is: ' + folderName)

    for subFolder in subFolders:
        print('The current subfolder is: ' + subFolder) 

    for filename in filenames: 
        print("File inside: ", filename)