a = 1.0
while a > 0.00000001:
    e = (1 + 2 * a)**(1/a)
    print("a =", a, "gir e =", round (e,7))
    a = a/10
