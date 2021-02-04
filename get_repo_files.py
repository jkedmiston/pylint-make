#!/usr/bin/env python
# https://stackoverflow.com/questions/8533202/list-files-in-local-git-repo
import sys
import subprocess

proc = subprocess.Popen(["git ls-tree --full-tree -r --name-only HEAD"],
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
files_in_repo = stdout.decode('utf-8').strip().split('\n')
final_files = list(filter(lambda x: x[-3:] == '.py', files_in_repo))
sys.stdout.write(' '.join(final_files) + '\n')
