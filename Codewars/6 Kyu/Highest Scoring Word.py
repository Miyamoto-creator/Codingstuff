def high(x):
    return [map(zip([ord(j) - 96 for i, j in (enumerate(h), i))) for i, h in enumerate(x.split())]