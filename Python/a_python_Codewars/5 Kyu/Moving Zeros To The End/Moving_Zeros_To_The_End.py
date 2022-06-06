def move_zeros(array):
    print(array)
    lst = []
    checker = []
    for i in array:
        if i == int(0):
            lst.append(True)
        elif not i == int(0):
            lst.append(False)
    for j in lst:
        if j == True:
            array.remove(0).append(0)
    print(checker)
    print(array)
    print(lst)
    return print(array)

move_zeros([1, 0, 1, 2, 0, 1, 3])
# should return [1, 1, 2, 1, 3, 0, 0]
