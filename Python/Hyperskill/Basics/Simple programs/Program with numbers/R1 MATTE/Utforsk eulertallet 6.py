t = 1.0
while t > 0.00000001:
    e = (1 + x * t)**(1/t)
    print("t =", t, "gir e =", round (e,7))
    t = t/10