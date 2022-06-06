duble_list = lambda X,Y : ([X*x for x in range(3)],[Y*y for y in range(3)]
                           Z*z for z in range(3))
print (duble_list(2,4))

duble_list = lambda X,Y, Z: ([X*x for x in range(3)],[Y*y for y in range(3)], [Z*z for z in range(3)])
list_A, List_B, list_C = duble_list(2,4, 6)
print (list_A)
print (List_B)
print (list_C)

