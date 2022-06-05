# Python3 program to find Integral
# points inside a triangle

# Class to represent an Integral
# point on XY plane.
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Utility function to find GCD of
# two numbers GCD of a and b
def gcd(a, b):
    if (b == 0):
        return a

    return gcd(b, a % b)


# Finds the no. of Integral points
# between two given points
def getBoundaryCount(p, q):
    # Check if line parallel to axes
    if (p.x == q.x):
        return abs(p.y - q.y) - 1
    if (p.y == q.y):
        return abs(p.x - q.x) - 1

    return gcd(abs(p.x - q.x),
               abs(p.y - q.y)) - 1


# Returns count of points inside the triangle
def getInternalCount(p, q, r):
    # 3 extra integer points for the vertices
    BoundaryPoints = (getBoundaryCount(p, q) +
                      getBoundaryCount(p, r) +
                      getBoundaryCount(q, r) + 3)

    # Calculate 2*A for the triangle
    doubleArea = abs(p.x * (q.y - r.y) +
                     q.x * (r.y - p.y) +
                     r.x * (p.y - q.y))

    # Use Pick's theorem to calculate
    # the no. of Interior points
    return (doubleArea - BoundaryPoints + 2) // 2


# Driver code
if __name__ == "__main__":
    p = Point(2, 1)
    q = Point(0, 3)
    r = Point(5, 4)

    print("Number of integral points "
          "inside given triangle is ",
          getInternalCount(p, q, r))
    print("Number of integral on"
          "the boundary", getBoundaryCount(p, q) + getBoundaryCount(q, r) + getBoundaryCount(r, p) + 3)
    print("Total number of points: ", getInternalCount(p, q, r) + getBoundaryCount(p, q) + getBoundaryCount(q, r) + getBoundaryCount(r, p) + 3)



# This code is contributed by rutvik_56