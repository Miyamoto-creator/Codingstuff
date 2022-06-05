def f(x):
    return x / (1+x**2)

svar1 = input("Velg verdi for x: ")
a = float(svar1)

svar2 = input("Velg verdi for delta x: ")
dx = float(svar2)

print("f(" + svar1 + ") er tilnærmet lik", round((f(a+dx))//(2*dx), 6))
