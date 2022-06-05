import numpy as np

def solution(x):
    n = np.arange(1, x)
    return n[(n % 3 == 0) | (n % 5 == 0)].sum()