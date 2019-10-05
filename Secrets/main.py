#!/usr/bin/env python

import credentials
import credentialreader

print("This is a simple demo app to externalize credentials from the app itself")
print(credentials.struser)

username = credentialreader.credentialreader(credentials.struser)
password = credentialreader.credentialreader(credentials.strpassword)

print("You user name is "+ username)
print("You password is " + password)
