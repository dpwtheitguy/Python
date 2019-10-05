#!/usr/bin/env python
# credentialreader.py
import codecs

def credentialreader(strSomeString):
  return codecs.decode(strSomeString, 'rot_13')