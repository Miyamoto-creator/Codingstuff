from sympy import symbols
from sympy.geometry import Point, Triangle, intersection, Polygon
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

bresenham(2, 1, 0, 3)


Trekant = Triangle(Point(2, 1), Point(0, 3), Point(5, 4))
print(Trekant)

placeholder = Point(0, 0)



