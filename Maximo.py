# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 23:14:44 2025

@author: Carlos Gil
"""

x=[5, 3, 2, 6, 2, 7]

maximo= x[0]

for numero in x:
    if numero > maximo:
        maximo = numero
        
print(maximo)