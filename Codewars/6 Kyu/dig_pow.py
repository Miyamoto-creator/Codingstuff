from math import sqrt

def dig_pow(n, p):
    result = 0
    for iter, num in enumerate(str(n)):
        result += int(num) ** p
        p += 1
    return result // n if result == n * (result // n) else -1

print(dig_pow(46288, 3))
print("Should return 51")