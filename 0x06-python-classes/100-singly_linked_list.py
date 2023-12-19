#!/usr/bin/python3
"""
Module: 100-singly_linked_list
Defines classes Node and SinglyLinkedList for a singly linked list.
"""


class Node:
    """
    Represents a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data: The data of the node (must be an integer).
            next_node: The next node in the list (must be a Node object or None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data of the node.

        Args:
            value: The data to be set (must be an integer).

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the next node in the list.

        Returns:
            Node: The next node in the list or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the next node in the list.

        Args:
            value: The next node to be set (must be a Node object or None).

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance with an empty list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value: The data of the new node (must be an integer).
        """
        new_node = Node(value)

        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the entire list.

        Returns:
            str: The string representation of the list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
