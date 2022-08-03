#!/usr/bin/python3

""" Return dict representation of a class Student"""


class Student:
    """ Class which represents a student """

    def __init__(self, first_name, last_name, age):
        """ Init new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return dictionary representation of Student"""
        return self.__dict__
