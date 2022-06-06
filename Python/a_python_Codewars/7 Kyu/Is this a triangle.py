import math

x1 = float(input("Gi x-verdi til punkt a: "))
y1 = float(input("Gi y-verdi til punkt a: "))

x2 = float(input("Gi x-verdi til punkt b: "))
y2 = float(input("Gi y-verdi til punkt b: "))

x3 = float(input("Gi x-verdi til punkt c: "))
y3 = float(input("Gi y-verdi til punkt c: "))

A = (x1, y1)
B = (x2, y2)
C = (x3, y3)

def is_triangle(A, B, C):
    if (A + B) * C / 2 > 0:
        if round(math.degrees(math.acos((B ** 2 + C ** 2 - A ** 2) / (2 * B * C)
                                        + (C ** 2 + A ** 2 - B ** 2) / (2 * C * A)
                                        + (A ** 2 + B ** 2 - C ** 2) / (2 * A * B)))) == 180:
            return True
print(is_triangle(A, B, C))

x1 = float(input("Gi x-verdi til punkt a: "))
y1 = float(input("Gi y-verdi til punkt a: "))

x2 = float(input("Gi x-verdi til punkt b: "))
y2 = float(input("Gi y-verdi til punkt b: "))

x3 = float(input("Gi x-verdi til punkt c: "))
y3 = float(input("Gi y-verdi til punkt c: "))

a = (x1, y1)
b = (x2, y2)
c = (x3, y3)


def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return "Punktene gir en Trekant"
    else:
        return "Punktene gir ikke en trekant"
print(is_valid_triangle(a, b, c))



# def is_valid_triangle(a,b,c):
#     if a+b>=c and b+c>=a and c+a>=b:
#         return True
#     else:
#         return False
#
# # Reading Three Sides
# side_a = float(input('Enter length of side a: '))
# side_b = float(input('Enter length of side b: '))
# side_c = float(input('Enter length of side c: '))
#
# # Function call & making decision
#
# if is_valid_triangle(side_a, side_b, side_c):
#     print('Triangle is Valid.')
# else:
#     print('Triangle is Invalid.')