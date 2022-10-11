#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square and init method that
sets its size.
"""

class Square():
     """Class Square that has attributes. Instantiation with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int'): A private instance size
        """
        self.__size = size
