#! /usr/bin/python3

import subprocess as sp
import sys
import time

f = open("run.sh", "w")
f.write("#! /bin/bash\n\n")
for x in range(int(sys.argv[1])):
    f.write("./musHistPractice.py 10\n")
    f.write("sleep 1\n")
    f.write("./termsPractice.py 10\n")
    f.write("sleep 1\n")
f.close()
sp.call("chmod +x run.sh", shell=True)
sp.call("./run.sh", shell=True)
