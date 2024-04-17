#!/usr/bin/python3
"""
This module defines a class Student that
represents a student.

Classes:
    Student: Represents a student with attributes such
    as first name, last name, and age.

Module Docstring:

    This module defines a class Student that represents a student.

Classes:
    Student: Represents a student with attributes such as
    first name, last name, and age.
"""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(self, attrs=None): Retrieves a dictionary
        representation of a Student instance with specified attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        with specified attributes.

        Args:
            attrs (list of str, optional): A list of attribute names to
            retrieve. Defaults to None.

        Returns:
            dict: A dictionary representation of the Student instance with
            specified attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
