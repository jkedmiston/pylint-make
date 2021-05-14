"""
Docstring here
"""
# pylint: disable=W0122


def run_cycle():
    """
    doc 2
    """
    while 1:
        exec(open('single_cycle.py').read())


if __name__ == "__main__":
    run_cycle()
