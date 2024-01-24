#!/usr/bin/python3
"""
In this module, we define classes for a
singly linked list (Node and SinglyLinkedList)
"""


class Node:
    """
    Node class representation for a singly linked list.

    Attributes:
    __data (int): Data of the node.
    __next_node (Node): Reference to the next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
        data (int): Data for the node.
        next_node (Node): Next node in the linked list. Defaults to None.

        Raises:
        TypeError: If data is not an integer or next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data of the node."""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:

            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next_node of the node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class representation.

    Attributes:

    __head (Node): Head of the linked list.

    """
    def __init__(self):

        """Simple instantiation of the SinglyLinkedList class."""

        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted
        position in the list (increasing order).

        Args:

        value (int): Value to be inserted into the linked list.

        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:

            new_node.next_node = self.__head

            self.__head = new_node
        else:
            current = self.__head

            while current.next_node is not None:
                if current.next_node.data < value:
                    break

                current = current.next_node
                new_node.next_node = current.next_node
                current.next_node = new_node

    def __str__(self):
        """Prints the entire linked list."""
        result = ""
        current = self.__head

        while current is not None:

            result += str(current.data) + "\n"
            current = current.next_node

            return result.strip()
