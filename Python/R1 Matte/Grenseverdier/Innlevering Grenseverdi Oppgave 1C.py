import numpy
def f(x):
    return 1 / x**2

counter = 0

while True:
    svar = input("Velg verdi for a: ")
    a = float(svar)

    t = 1
    while t > 0.00001:
      print("f(" + str(round( a - t, 7)) + ") = ", round(f(a - t), 7))
      t = t/10

    t = 1
    while t > 0.00001:
      print("f(" + str(round(a + t, 7)) + ") = ", round(f(a + t), 7))
      t = t/10
      #print(f"T is: {t}")
