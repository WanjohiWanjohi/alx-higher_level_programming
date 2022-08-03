""" Read UTF8 encoded file"""


def read_file(filename=""):
    ''' Print file contents to stdout '''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
