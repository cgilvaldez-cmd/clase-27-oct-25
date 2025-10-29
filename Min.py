# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 16:06:12 2025

@author: Carlos Gil
"""

x= [5, 3, 2, 6, 2, 7]

minimo= x[0]

for numero in x:
    if numero < minimo:
        minimo = numero
        
print(minimo)
