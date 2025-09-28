# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 08:20:22 2025

@author: El-Wattaneya
"""

def innermost_list_plus_one(input_list):
# if there are no further innermost lists, it will return a list with one added to each element
    if not any(isinstance(i, list) for i in input_list):
        return [x + 1 for x in input_list]
    for element in input_list:
# if there is another innermost list, the function will call itself to check this innermost list again (Recursion Case)
        if isinstance(element, list):
            return innermost_list_plus_one(element)

# now we try with an example
input_list = [1, 2, 3, 4, [5, 6, 7, [8, 9]]]

print(innermost_list_plus_one(input_list))  
