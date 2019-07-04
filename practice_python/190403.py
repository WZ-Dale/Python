# -*-coding: utf-8 -*-

import numpy as np

a = np.array([[ 2, 7, 4, 2],
       [35, 9, 1, 5],
       [22, 12, 3, 2]])

print(a)

a = a[a[:,-1].sort()]

print(a)
