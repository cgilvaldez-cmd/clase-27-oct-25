# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 16:31:03 2025

@author: Carlos Gil
"""

x=[5, 3, 2, 6, 2, 7]

def ordenamiento(x):
    n = len(x)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if x[j] < x[minimo]:
                minimo = j
        
        x[i], x[minimo] = x[minimo], x[i]
    return x

print(ordenamiento(x))
    
