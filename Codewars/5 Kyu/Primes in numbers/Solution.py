def primes(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(f"{d}")
            n //= d
        d += 1
    if n > 1:
        primfac.append(str(n))
    list_element = sorted(set([int(i) for i in primfac]))
    value = [sorted(primfac).count(str(i)) for i in list_element]
    prev = []
    for i, n in enumerate(list_element):
        if int(value[i]) > 1:
            prev.append(f"({str(list_element[i])}**{str(value[i])})")
        else:
            prev.append(f"({str(list_element[i])})")
    return "".join(prev)

print(primes(7775460))


"""
def primes(n):
    primfac = []
    d = 2
    while d * d <= n:
        modulo = (n % d)
        while (n % d) == 0:
            primfac.append(f"{d}")  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(str(n))
    return primfac

def modify(value):
    list_element = sorted(set([int_value:=int(i) for i in value]))
    value = [sorted(value).count(str(i)) for i in list_element]
    prev = []
    for i, n in enumerate(list_element):
        if int(value[i]) > 1:
            prev.append(f"({str(list_element[i])}**{str(value[i])})")
        else:
            prev.append(f"({str(list_element[i])})")
    return "".join(prev)

value = primes(7775460)
print(modify(value))

    q = __import__("functools").partial(__import__("os")._exit, 0)  # FIXME
    __import__("IPython").embed()  # FIXME        
        if value[i] == value[i+1] and i < len(value):
            lst.append(value[i] + value[i+1])
            lst.count(value[i])"""