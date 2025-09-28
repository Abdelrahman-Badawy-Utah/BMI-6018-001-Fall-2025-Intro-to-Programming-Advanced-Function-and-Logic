# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 08:49:33 2025

@author: El-Wattaneya
"""

# The following function takes two arguments: the input list and the user-defined threshold
def filter_function_with_threshold(input_list, threshold):
# created an empty list to store the results
    result = []  
    for x in input_list: #it loops through each element in the input list
        if x <= threshold:  # then check if x is less than or equal to threshold
            result.append(x)  # if less than or equal to the threshold, it will be added to the result list
    return result  # return the full list after the loop finishes
    
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
threshold = 6
print(filter_function_with_threshold(input_list, threshold))  