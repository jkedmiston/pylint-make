# Overview
This repository demonstrates a mechanism to run `pylint` on a large python project.

# Features
* Every python file under repository control is run through `pylint` using the rules in `.pylintrc`. When the file passes, a dummy file with extension `.pylint` is written so that `pylint` is only rerun on the file if the source code in that file changes.
* Python files not under repo control are not checked under `pylint`.

# Demo
* Copy the dummy python file `stray_python_file.py.example` to `stray_python_file.py`. This demonstrates the presence of a non-repo controlled python file.
* Type `make`.
* One should see output similar to
```
jedmiston@macbook: pylint-make$ make
pylint -rn not_passes_pylint.py
************* Module not_passes_pylint
not_passes_pylint.py:5:0: W0611: Unused import os (unused-import)

------------------------------------------------------------------
Your code has been rated at 6.67/10 (previous run: 6.67/10, +0.00)

make: *** [Makefile:13: not_passes_pylint.pylint] Error 4
```