
# example from Linux Academy fixes. 

import subprocess 
import sys

cmdping = "ping -c 1 192.168.1."

for x in range(2, 15):
	p = subprocess.Popen(cmdping + str(x), shell=True, stderr=subprocess.PIPE)
	print(p.stderr.read(1))

	while True:
		out = p.stderr.read(1)
		if out == '' and p.poll() != None:
			break
		if out != '':
			sys.stdout.write(str(out))
			sys.stdout.flush()
