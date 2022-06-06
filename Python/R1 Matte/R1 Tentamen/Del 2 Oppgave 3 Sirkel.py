from math import sqrt

def circle(a, b, radius, s, t):
    def avstand_punkt(x_1, y_1, x_2, y_2):
        return round(sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2), 1)

    avstand = avstand_punkt(a, b, s, t)
    if avstand > radius:
        return f"D = {avstand} og Punktet {[s, t]} ligger utenfor sirkelen"
    elif avstand == radius:
        return f"D = {avstand} og Punktet {[s, t]} ligger på sirkelen"
    elif avstand < radius:
        return f"D = {avstand} og Punktet {[s, t]} ligger innenfor sirkelen"

print(circle(25.0, -20.0, 3.0, 22.0, -20.0), "Ønsket resultat = På")
print(circle(25, -20, 3, 20, -20), "Ønsket resultat = Utenfor")
print(circle(25, -20, 3, 25, -20), "Ønsket resultat = Innenfor")
print(circle(25.0, -20.0, 3.0, 27.89, -20.79), "Ønsket resultat = På")
print(circle(25, -20, 3, 28, -20), "Ønsket resultat = På")
print(circle(25, -20, 3, 27.58, -21.54), "Ønsket resultat = På")

"""def sirkel(a, b, r):
    sentrum = np.array([a, b])
    diameter = r * 2
    return min([i for i in combinations_with_replacement(sentrum, r)])"""
"""def circle(a, b, radius, s, t):
    if (-radius + a) < s < (radius + a) and (-radius + b) < t < (radius + b):
        return ("Punktet ligger innenfor sirkelen")
    elif (-radius + a) <= s <= (radius + a) and (-radius + b) <= t <= (radius + b):
        return ("Punktet ligger på sirkelen")
    else:
        return ("Punktet ligger utenfor sirkelen")

            def lengde(x, y):
        return round(sqrt((x)**2 + (y)**2), 1)"""
# print(sirkel(1, 4, 2))
