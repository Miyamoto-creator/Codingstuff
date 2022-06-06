def century(year):
    x = 1
    while year >= x:
        x = x + 100
    return int(x/100)

print(century(6001))