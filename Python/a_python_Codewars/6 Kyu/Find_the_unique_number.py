import numpy as np

def find_uniq(arr):
    unique, counts = np.unique(arr, return_counts = True)
    return unique[counts==1]

https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python