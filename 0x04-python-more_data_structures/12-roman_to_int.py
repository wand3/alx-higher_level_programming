#!/usr/bin/python3

def roman_to_int(roman_string):
    """ converts a roman numeral character into its respective integer """
    if roman_string is None or type(roman_string) is not str:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    roman_list = list(roman_string.upper())
    result = 0
    prev = 0
    for i in roman_list:
        if i in roman_dict:
            result += roman_dict[i]
            if roman_dict[i] > prev:
                result -= prev * 2
            prev = roman_dict[i]
        else:
            return 0
    return result
