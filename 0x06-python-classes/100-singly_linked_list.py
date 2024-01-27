#!/usr/bin/python3

"""
This module defnes two classes: Node and SinglyLinkedList.

Node class represents a node of a singly linked list.
It has private instance attributes:
- __data (int): Data of the node.
- __next_node (Node): Next node in the linked list.

SinglyLinkedList class represents a singly linked list.
It has a private instance attribute:
- __head: Head of the linked list.

The module privides the following functionality:
- Creating nodes with the Node class.
- Creating and manipulating singly linked lists with
    the SingltLinkedList class.
"""


class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
    - __data(int): Private instance attribute representing
                   the data of the node.
    - __next_node (Node): Private instance attribute representing
                          the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Constructor method for the Node class.

        Parameters:
        - data (int): Data for the node.
        - next_node (Node, optional): Next node in the linked list.
                                      default is None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data of the node.
        """

        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data of the node.

        Parameters:
        - value (int): Data to set.

        Raises:
        -- TypeError: if data is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next node in the linked list.
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node in the linked list.

        Parameters:
        - value (Node): Next node to set.

        Raises:
        - TypeError: If next_node is not a Node object.
        """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
    - __head: Private instance attribute representing the head of
            the linked list.
    """

    def __init__(self):
        """
        Constructor method for the SinglyLinkedList class.
        """

        self.__head = None

    def sorted_insert(self, value):
        """
        Public method to insert a new Node into the correct
                sorted position in the list (increasing order).

        parameters:
        - value (int): Data for the new node.
        """

        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        String representation of the linked list.
        """
        result = []
        current = self.__head

        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
