from itertools import combinations
import numpy as np


def boucleEchange(n):
    co = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            co += 1
    print(co)


def boucleInsere(n):
    co = 0
    positionArray = np.empty((0, 2), int)
    # positionArray = np.zeros((n*n - 2*n + 1, 2))
    for i in range(1, n + 1):
        j = 1
        while j < n + 1:
            if j == i or j == i - 1:
                j += 1
            else:
                positionArray = np.append(positionArray, np.array([[i, j]]), axis=0)
                j += 1
                co += 1
    return positionArray, co
"""
arr0 = np.zeros([3, 3, 2], dtype=str)
arr = np.array([[[1, 2], [3, 4], [5, 6]], [['a', 'b'], ['c', 'd'], ['e', 'f']]])
#arr = np.concatenate((arr0, [[['A', 'B'], ['C', 'D'], ['E', 'F']]]), axis=0)
arr0[0] = np.array([['A', 'B'], ['C', 'D'], ['E', 'F']])
arr0[1] = np.array([['G', 'H'], ['I', 'J'], ['K', 'L']])
arr0[2] = np.array([['M', 'N'], ['O', 'P'], ['Q', 'R']])

print(arr0[0])
#print(arr.shape)
"""

idx = np.random.randint(2)
print(idx)
