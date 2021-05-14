"""
Inner loop to cycle, while cycle is running, one can make edits here if needed
"""
# pylint: disable=C0103
import subprocess
import time
proc_to_run = subprocess.Popen(["make"], shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc_to_run.communicate()
print("stdout: %s" % stdout.decode('utf-8'))
print("stderr: %s" % stderr.decode('utf-8'))
time.sleep(1)
