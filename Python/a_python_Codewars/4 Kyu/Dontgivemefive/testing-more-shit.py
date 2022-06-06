import numpy as np
from collections import Counter

import re


def jimmy_neutron(start, end):
    count = lambda n: int(re.sub(r'5(\d*)', lambda m: '4' + '9' * len(m[1]), str(n)).translate(str.maketrans("56789", "45678")), 9)
    if start > 0:
        return count(end) - count(start - 1)
    elif end < 0:
        return count(-start) - count(-end - 1)
    else:
        return count(end) + count(-start) + 1

"""for i in range(100):
    print(f"Iteration: {i} Value: {10 ** i - jimmy_neutron(1, 10 ** i)}")"""
lst = []
x = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
teller = 0
for i in range(100000):
    print(f"Iteration: {i} Value: {str(jimmy_neutron(1, 10 ** i))[0]} ... Len: {len(str(jimmy_neutron(1, 10 ** i)))}")
    lst.append(str(jimmy_neutron(1, 10 ** i))[0])
#print(lst)
print("====================")
y = [lst.count(str(i)) for i in range(1, 10)]
result = dict(zip(x, y))

array = np.array(list(result.items()), dtype=dtype)
print(array)


""" if str(jimmy_neutron(1, 10 ** i))[0].count(str(jimmy_neutron(1, 10 ** i))[0]) == 1:
    count = str(jimmy_neutron(1, 10 ** i))[0].count(str(jimmy_neutron(1, 10 ** i))[0])
    print(str(jimmy_neutron(1, 10 ** i))[0], count)"""

""" 
1: 27
2: 16
3: 13
4: 11
5: 9
6: 7
7: 7
8: 5
9: 5
"""