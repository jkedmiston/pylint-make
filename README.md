# Overview
This repository demonstrates a mechanism to run `pylint` on a large python project.

# Features
* Every python file under repository control is run through `pylint` using the rules in `.pylintrc`. When the file passes, a dummy file with extension `.pylint` is written so that `pylint` is only rerun on the file if the source code in that file changes.
* Python files not under repo control are not checked under `pylint`.

# Demo
* Copy the dummy python file `local_dummy.py.example` to `local_dummy.py`. This demonstrates the presence of a non-repo controlled python file.
* Type `make`. 