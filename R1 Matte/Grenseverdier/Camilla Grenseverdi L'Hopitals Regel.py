def f(x):
    return x**2 - 3*x - 4

def g(x):
    return x - 4

while True:
    dx = 0.00000001

    svar1 = (input("Hvilken verdi nærmer x seg?: "))
    a = float(svar1)

    print(f"grenseverdien når x nærmer seg "+ svar1 +" er tilnærmet = ",
          round((( f(a+dx) - f(a-dx))/ 2*dx) / (( g(a+dx) - g(a-dx)) / 2*dx), 6))