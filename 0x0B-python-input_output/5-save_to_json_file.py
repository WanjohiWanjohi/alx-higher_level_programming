#!/usr/bin/python3

""" Write an OBJECT as JSON to a file"""

import json


def save_to_json_file(my_obj, filename):
    """ Write an object to a file as JSON string"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
