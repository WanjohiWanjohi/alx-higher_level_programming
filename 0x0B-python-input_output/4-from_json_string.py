#!/usr/bin/python3

""" Return Python object from JSON string"""
import json


def from_json_string(my_str):
    """
    Return a python DS from a JSON string
    Args:
    my_str: string to convert to object
    """
    return json.loads(my_str)
