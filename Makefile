# https://stackoverflow.com/questions/23139933/how-to-write-a-makefile-to-run-pylint
# the touch at the end of the command makes it so that only changed files get re-linted 
PYLINT = pylint
PYLINTFLAGS = -rn
PYTHONFILES=$(shell python get_repo_files.py)

# PYTHONFILES := $(wildcard *.py)
all: pylint

pylint: $(patsubst %.py,%.pylint,$(PYTHONFILES))

%.pylint:
	$(PYLINT) $(PYLINTFLAGS) $*.py
	touch $*.pylint

clean:
	echo $(PYTHONFILES)
