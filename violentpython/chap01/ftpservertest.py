#/usr/bin/enc python
# ftpservertest.py
# Labbing Chap 1 page 10 Socket test 
# Orgiginal was in Python 2 converting to 3

import socket

socket.setdefaulttimeout(2)
s = socket.socket()

# can I use DNS name? Will this work with TFTP?
#s.connect(('ftp://ftp-srv2.kddilabs.jp', 21))

s.connect(('202.255.47.226', 21))
ans = s.recv(1024)

# what is in the ans variable?
# print(ans)
# print(type(ans))

# can we cast ans to str? YES WE CAN!
ans = str(ans)

# Get rid of the annoying byte prefix
ans = ans[2:]

print(ans)
if ("some string" in ans):
    print("Some string was found in the banner")
elif ("FTP blah" in ans):
    print("FTP blah found")
else:
    print("No Vuln found")

