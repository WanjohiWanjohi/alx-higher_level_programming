#!/usr/bin/python3

""" Return dict representation of a class Student"""


class Student:
    """ Class which represents a student """

    def __init__(self, first_name, last_name, age):
        """ Init new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return dictionary representation of Student"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of a STudent instance """
        for k, v in json.items():
            setattr(self, k, v)
