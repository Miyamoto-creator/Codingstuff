from operator import add

def add(a, b):
    a = list(str(a))
    b = list(str(b))
    l = [x + y for x, y in zip(a, b)]
    print(l)
    """total = len(a) - len(b)
    print(total, str(a), str(b))
    lst = []
    lst.append(a + b)
    lst = "".join(lst)
    length = len(lst)
    print(lst, len(lst))"""
add(122, 81)
'''should add up to 1103

 1 2 2
+  8 1
= 1 10 3'''



'''for j in range(len(c)) :
      st_a[j] = st_a[j] * 10 ** j'''

# 1 * 10 + 1 * 10 = første del
# andre del er b plusset på a delen
# go do it brooo