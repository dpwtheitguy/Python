#/user/bin/env python
# tryexcept.py

intNum = ""
try:
    intNum = int(input())
    print(intNum)
except:
    print("Well that didn't work")