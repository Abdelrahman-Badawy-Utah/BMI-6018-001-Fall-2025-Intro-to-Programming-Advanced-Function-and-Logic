# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 15:40:57 2025

@author: El-Wattaneya
"""

#1. Import numpy as np and print the version number.
## importing the numpy
import numpy as np
## printing the version
print(np.__version__)



#2. Create a 1D array of numbers from 0 to 9. 
np.arange(0,10)



#3. Import a dataset with numbers and texts keeping the text intact in python numpy.
## URL of the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
## Loading the dataset, keeping text intact
iris_data = np.genfromtxt(url, delimiter=',', dtype=None, encoding='utf-8')
# Checking the data
print(iris_data)



#4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset.
# Loading the first four columns (the numeric columns)
iris_data = np.genfromtxt(url, delimiter=',', usecols=(0,1,2,3), dtype=float)
# 4th column is petal width
petal_width = iris_data[:, 3]
# Finding positions where petal width > 1.0
positions = np.where(petal_width > 1.0)[0]
# the first position will be at index 0
first_position = positions[0]
print("The first occurrence of petal width > 1.0 is at row:", first_position)



#5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10.
np.random.seed(100)
a = np.random.uniform(1,50, 20)
# i will use the mask
# replacing values >30 with 30
a[a > 30] = 30
# replacing values <10  with 10
a[a < 10] = 10   

print(a)
