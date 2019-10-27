#/usr/bin/env python
# lists.py

import copy

lstMylist  = ["test", "hello", "world"]

for i in range(len(lstMylist)):
    print(lstMylist[i])

lstMylist.append("yo")

lstMylist.sort(reverse=True)
print(lstMylist)

lstSortedList = sorted(lstMylist)
print(lstSortedList)

# Copying alist
lstCopy = copy.copy(lstMylist)
lstCopy.append("copied")

print(lstMylist)
print(lstSortedList)
print(lstCopy)
print(lstCopy.index("test"))