#!/usr/bin/python3

""" Create an object from JSON stream"""
import json


def load_from_json_file(filename):
    """
    Return JSOn representation of string
    """
    with open(filename, "r") as f:
        return json.load(f)
