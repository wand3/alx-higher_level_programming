#!/usr/bin/python3
"""Square class model that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class Constructor for Square

        Attribute:
            size (int): The size of the square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ string representation of a square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
