#!/usr/bin/python3
"""
This module defines a Node class.
"""


class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): Reference to the next
        node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Parameters:
            data (int): The data to be stored in the node.
            next_node (Node, optional): Reference to the
            next node. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node
            is not None or a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data stored in the node.

        Parameters:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the next node in the linked list.

        Parameters:
            value (Node or None): The next node in the linked list.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance
        with an empty list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list (increasing order).

        Parameters:
            value (int): The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None\
                    and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: String representation of the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
