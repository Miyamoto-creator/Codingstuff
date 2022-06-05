import math


def f(x):
    return x / (10+x**2)
# (x**2 - 5*x + 4) / (2*x - 2)

print(math.sqrt(f(1)))
while True:
    dx = 0.00000001

    svar1 = (input("Hvilken verdi nærmer x seg?: "))
    a = float(svar1)

    print(f"grenseverdien når x nærmer seg "+ svar1 +" er tilnærmet = ",
          round((( f(a+dx) - f(a-dx))/ 2*dx) / (( f(a+dx) - f(a-dx)) / 2*dx), 6))
