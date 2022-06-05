def f(x):
    return (x**2-1) / (x**2-x)

svar = input("Velg verdi for a: ")
a = float(svar)
info = f(a) * 0.7**5
print(info)

t = 0.5
while t > 0.00001:
  print("f(" + str(round( a - t, 7)) + ") = ", round(f(a - t), 7))
  t = t/10

t = 0.5
while t > 0.00001:
  print("f(" + str(round(a + t, 7)) + ") = ", round(f(a + t), 7))
  t = t/10
