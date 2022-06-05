import numpy as np

def is_isogram(string):
    unique, counts = np.unique([x.lower() for x in string], return_counts = True)
    return not any(unique[counts>1])

# https://www.codewars.com/kata/54ba84be607a92aa900000f1
