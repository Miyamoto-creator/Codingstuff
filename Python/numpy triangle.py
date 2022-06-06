import numpy as np

""" expected output 
[ [0,0,0,0,0,0],
  [0,0,1,0,0,0],
  [0,1,1,1,0,0],
  [1,1,1,1,1,0],
  [0,0,0,0,0,1],
  [0,0,0,0,0,0] ]"""
triangle = ((2,1), (0, 3), (5, 4))

A, B, C = np.array(triangle[0]), np.array(triangle[1]), np.array(triangle[2])
AB, AC = B - A, C - A
BC, BA = C - B, A - B
CA, CB = A - C, B - C
vectors = [AB, AC, BC, BA, CA, CB]
print(AC)
test = np.diag(AB)
test1 = np.diagonal(BC)
test2 = np.diag(AC)
tester = np.diagonal(vectors)
print(test)
print("hitler ",test1)

#gr = np.array((input("Skriv k: ")))
hitlers = np.tri(6, 6, like=test)
hitlers1 = np.tri(6, 6, like=test1)
hitlers2 = np.tri(6, 6, like=test2)

ultimate_hitler = np.tri(6, 6, like=test1)
#ultimate_hitler = np.tri(6, 6, -4)


print(ultimate_hitler.flip)