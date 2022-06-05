from numpy import array


# Vektor a
x1 = float(input("x1 ="))
y1 = float(input("y1 ="))
a = array([x1, y1])

# Vektor b
x2 = float(input("x2 ="))
y2 = float(input("y2 ="))
b = array([x2, y2])

c = b - a

print("Vektor c = ", c)
