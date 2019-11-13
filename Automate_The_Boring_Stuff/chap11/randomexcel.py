#!/usr/bin/env python
# randomexcel.py
# pip install openpyxl

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))

# example doesn't , but this did. 
print(wb.sheetnames)

# Find sheets this way
sheet = wb['Sheet1']
print(sheet)

print(sheet['A1'].value)

c = sheet['B1']
print(c.value)
