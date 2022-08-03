#!/usr/bin/python3

""" returns a dictionary description  with
simple data structure  for Json serialization"""


def class_to_json(obj):
    """ Returns JSon representation of object
    """
    return obj.__dict__
