# -*- coding: utf-8 -*-
"""Set_Operations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14kYj34MsKFQio4EJuWjup4q-S5LccAd7
"""

#Declaring two sets
E = {1, 2, 3, 4, 5}
N = {0, 2, 4, 6, 8}

#Operations on sets
union=E.union(N)
intersection=E.intersection(N)
difference=N.difference(E)
symmetric_difference=E.symmetric_difference(N)

#Printing the output
print("Union of E and N is", union)
print("Intersection of E and N is", intersection)
print("Difference of E and N is", difference)
print("Symmetric difference of E and N is", symmetric_difference)