def f(x):
    return (3*x+4)/(x**2-3)

# x/(100+x**2)

h = 0.0001
x = 0
while (f(x+h)-f(x))/h > 0:
    x = x + 0.01
    print((f(x+h)-f(x))/h)
print("x =", x)