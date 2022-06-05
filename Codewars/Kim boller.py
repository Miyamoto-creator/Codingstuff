import numpy as np
from numpy import array

nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)
xv
array([[0. , 0.5, 1. ],
       [0. , 0.5, 1. ]])
yv
array([[0.,  0.,  0.],
       [1.,  1.,  1.]])
xv, yv = np.meshgrid(x, y, sparse=True)  # make sparse output arrays
xv
array([[0. ,  0.5,  1. ]])
yv
array([[0.],
       [1.]])



xv, yv = np.meshgrid(x, y, indexing='ij')
for i in range(nx):
    for j in range(ny):
        treat xv[i,j], yv[i,j]

xv, yv = np.meshgrid(x, y, indexing='xy')
for i in range(nx):
    for j in range(ny):
        treat xv[j,i], yv[j,i]