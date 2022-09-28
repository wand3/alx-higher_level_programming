#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """ return a new dictionary with all values multiplied by2 """
    return {key: val * 2 for (key, val) in a_dictionary.items()}
