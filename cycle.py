import sys
import os
import subprocess
import time
while 1:
    p = subprocess.Popen(["make"], shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    print("stdout %s" % stdout.decode('utf-8'))
    print("stderr %s" % stderr.decode('utf-8'))
    time.sleep(10)
