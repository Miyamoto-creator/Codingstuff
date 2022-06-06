def longest(a1, a2):
    a1 += a2
    a3 = []
    a3.append(a1)
    a3 = list(dict.fromkeys(a1))
    a3.sort()
    return a3
