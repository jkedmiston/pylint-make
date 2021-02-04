#!/usr/bin/env python
"""
Based on the git command here, then filters for python files.
https://stackoverflow.com/questions/8533202/list-files-in-local-git-repo
"""
import sys
import subprocess


def get_git_python_files():
    """
    Get a list of all files in repository control, then filter the
    python files, and write to stdout, similar to an ls command.
    """
    proc = subprocess.Popen(["git ls-tree --full-tree -r --name-only HEAD"],
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdout, _ = proc.communicate()
    files_in_repo = stdout.decode('utf-8').strip().split('\n')
    final_files = list(filter(lambda x: x[-3:] == '.py', files_in_repo))
    sys.stdout.write(' '.join(final_files) + '\n')


if __name__ == "__main__":
    get_git_python_files()
