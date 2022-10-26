#!/usr/bin/python3
"""
Contains definiton for the class MyList that inherits from list.
"""


class MyList(list):
    """
     class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        sortedlist = sorted(self)
        print(sortedlist)
