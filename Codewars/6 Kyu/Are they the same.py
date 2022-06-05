import math

def comp(array1, array2):
    try:
        return sorted([x ** 2 for x in array1]) == sorted(array2)
    except TypeError:
        return False