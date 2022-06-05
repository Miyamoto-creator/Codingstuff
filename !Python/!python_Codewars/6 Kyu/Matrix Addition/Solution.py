matrix1 = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1]
]

matrix2 = [
    [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3]
]

import numpy as np



def matrix_addition(a, b):
    arr = []
    for x in range(len(a)):
        value = {0} * len(a)
        for y in range(len(a[0])):
            value[x][y] = a[x][y] + b[x][y]
        arr.append(value)
    return arr




print("Actual Output: \n",matrix_addition(matrix1, matrix2))
print("Expected output: \n"
    f"[\n"
    f"[3, 4, 4],\n"
    f"[6, 4, 4],\n"
    f"[2, 2, 4] \n"
      f"]")

A = [[12,7,3],

    [4 ,5,6],

    [7 ,8,9]]

B = [[5,8,1],

    [6,7,3],

    [4,5,9]]

result = [[0,0,0],

         [0,0,0],

         [0,0,0]]

# iterate through rows

for x in range(len(A)):

   # iterate through columns

   for y in range(len(A[0])):

       result[x][y] = A[x][y] + B[x][y]

for q in result:

   print(q)