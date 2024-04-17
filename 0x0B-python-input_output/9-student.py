#!/usr/bin/python3
"""
This module defines a class Student that represents
a student.

Classes:
    Student: Represents a student with attributes such
    as first name, last name, and age.
"""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(self): Retrieves a dictionary representation
        of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with first_name,
        last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of
        a Student instance.

        Returns:
            dict: A dictionary representation
            of the Student instance.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
