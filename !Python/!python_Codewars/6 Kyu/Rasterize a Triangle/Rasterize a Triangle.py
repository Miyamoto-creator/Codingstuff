test = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]

import numpy as np
import math


def bresenham(x1, y1, x2, y2):
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    for x in range(x1, x2 + 1):

        print("(", x, ",", y, ")\n")

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new

        # Slope error reached limit, time to
        # increment y and update slope error.
        if (slope_error_new >= 0):
            y = y + 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)


# driver function

bresenham(2, 1, 0, 3)
bresenham(0, 3, 5, 4)
bresenham(2,1, 5, 4)

# This code is contributed by ash264

triangle = ((2,1), (0, 3), (5, 4))
def draw_triangle(triangle, n):
    def lengde(vector):
        return math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    def getIntersection(s):
        """ return an intersection from a set of lists """
        i = set(s[0])
        for x in s[1:]:
            i = i & set(x)
        return i
    """Fullfør denne oppgaven ved hjelp av dictionary!!"""
    A, B, C = np.array(triangle[0]), np.array(triangle[1]), np.array(triangle[2])
    AB, AC = B - A, C - A
    BC, BA = C - B, A - B
    CA, CB = A - C, B - C
    vectors = [AB, AC, BC, BA, CA, CB]
    print("test: ",getIntersection(vectors))


    lst = [[str(i)]*n for i in range(n)]
    print(lst)
    for x, y in triangle:
        for i, k in enumerate(lst):
            print(y, i)
            if i == y:
                lst[y][x] = '#'
    y_triangle = [y for x, y in triangle]

    # while True:
    #     for x, y in triangle:
    #         if y == lst[counter]:
    #             lst[y][x] += 1
    #     if counter == n:
    #         counter = 0
    #     elif Amount == 0:
    #         break
    #     counter += 1
    #     Amount -= 1
    print(np.tri(6, 6, like=AB))
    print(np.triu(np.arange(3 * 4 * 5).reshape(3, 4, 5)))

    def my_func(a):
        """Average first and last element of a 1-D array"""
        return (a[0] + a[-1]) * 0.5

    print("test", my_func(AB))
    b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(np.apply_along_axis(my_func, 0, b))
    return '\n'.join([i for i in list(map(str, lst))])
print(draw_triangle(triangle, 6))



#     for iter, (x, y) in enumerate(triangle):
#         print(iter)
#         for i, elem in enumerate(lst):
#             if i == x:
#                 lst[y][x] = 1
#     return '\n'.join([i for i in list(map(str, lst))])
# return '\n'.join([', '.join(i) for i in greg])
# while True:
#     if Amount >= (index - 1):
#         Change[counter] += index - 1
#         Amount -= index - 1
#         counter -= 1
#         continue
#     elif Amount == 0:
#         break
#     index -= 1
# print(Change)
# return "".join([chr(i + 96) for i in Change])


# triangle = ((2,1), (0, 3), (5, 4))
# def draw_triangle(triangle, n):
#     """Fullfør denne oppgaven ved hjelp av dictionary!!"""
#     coord_x, coord_y = "", ""
#     for i in range(n):
#         coord_x += 'x' + f'{i} '
#         coord_y += 'y' + f'{i} '
#     coord_xy = list(zip(coord_x.split(), coord_y.split()))
#     print(coord_xy)
#     #print(coord_x.split(), coord_y.split())
#     y_list = {}
#     x_list = []
#     for i, (x, y) in enumerate(coord_xy):
#         y_list[y] = '0' * n
#         # x_list[x] = x_list.setdefault(x), y_list[y].items()
#     test = {}
#     for i, (x, y) in enumerate(coord_xy):
#         test[coord_x.split()[i]] = [" ".join(i) for i in y_list[y]]
#     print(coord_x.split())
#     print(x_list)
#
#     print(test)
#     print(coord_x)
#     lst = []
#     num = 0
#     greg = []
#     for i in range(n, n*n+1):
#         str += '0'
#         if i % n == 0:
#             lst.append(str.split(" "))
#             str = ''
#     #print(greg)
#
#     for i, k in enumerate(lst):
#         for iter, j in enumerate(k):
#             greg.append(" ".join(j))
#     greg = [i.split() for i in greg]
#     for x, y in triangle:
#         #print("test", x, y)
#         for iter, k in enumerate(greg[y]):
#             #print(iter)
#             if iter == x:
#                 greg[y][iter] = int(greg[y][iter])
#                 greg[y][iter] += 1
#     print(greg)
#     return '\n'.join([', '.join(i) for i in greg])
# print(draw_triangle(triangle, 6))