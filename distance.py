#!/usr/bin/python

import numpy as np

def euclidean_distance(x,y):
    return np.linalg.norm(x-y)
    
    
x = np.array([1,2])
y = np.array([2,3])
print(euclidean_distance(x,y))
