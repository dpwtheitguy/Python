#!/usr/bin/env python
# chap10 stuff
import traceback


#try:
#    raise Exception("This is the error message")
#except:
#    errorFile = open("errorinfo.txt", 'w')
#    errorFile.write(traceback.format_exc())
#    errorFile.close()
#    print("traceback written")

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'the pod bay door need to be open '

podBayDoorStatus = 'opeclosedn'
assert podBayDoorStatus == 'open', 'the pod bay door need to be open '