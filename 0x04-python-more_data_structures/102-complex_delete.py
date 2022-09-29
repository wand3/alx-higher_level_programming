#!/usr/bin/python3

def complex_delete(a_dictionary, value):
   """ deletes keys with aspecific value in a dictionary """
    for key, val in list(a_dictionary.items()):
        if val == value:
            a_dictionary[key]
    return a_dictionary
