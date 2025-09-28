# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 07:58:16 2025

@author: El-Wattaneya
"""

my_list = [1, 2, 3, 4, [5, 6, 7, [8, 9]]]

while True:
#first, we check if the last element is a list     
    if isinstance(my_list[-1], list):
        my_list = my_list[-1]  # and if the last element is a list, it should assign my_list to the innermost list
    else:
        break  # it will break the loop if there are no more innermost lists

# now we add 1 to each element inside the innermost list (my_list) 
result = [x + 1 for x in my_list]

print(result)  