def f(x):
  if x < 1:
    return x**2 + 2
  else:
      return -2*x + 5

svar = input("Velg verdi for a:")
a = float(svar)

t = 1.0
while t > 0.00001:
  print("f(" + str(round( a - t, 7)) + ") = ", round(f(a - t), 7))
  t = t/10

t = 1.0
while t > 0.00001:
  print("f(" + str(round(a + t, 7)) + ") = ", round(f(a + t), 7))
  t = t/10
