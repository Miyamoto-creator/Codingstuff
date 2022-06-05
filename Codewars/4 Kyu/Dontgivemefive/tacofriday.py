"""def dont_give_me_five(start,end):
    def count(value,x=0,num=0):
        arr = [x := int((10 ** (n-1))+ x * 9) for n in range(0,len(str(value)))]
        for i in range(len(str(value)),0,-1):
            if i > 0 and (y := (value % 10**(i))//10**(i-1)) != 0:
                num += arr[i-1] * y
                if y == 5:
                    if i != 1: num += (value % (10**(i-1)))
                    return num
                if y > 5:
                    num += 10**(i-1)-arr[i-1]
        return value - num
    if start > 0:
        return count(end) - count(start - 1)
    elif end < 0:
        return count(-start) - count(-end - 1)
    else:
        return count(end) + count(-start) + 1"""

import re

def dont_give_me_five(start, end):
    count = lambda n: int(re.sub(r'5(\d*)', lambda m: '4' + '9' * len(m[1]), str(n)).translate(str.maketrans("56789", "45678")), 9)
    if start > 0:
        return count(end) - count(start - 1)
    elif end < 0:
        return count(-start) - count(-end - 1)
    else:
        return count(end) + count(-start) + 1


print(dont_give_me_five(-17, 9))
print(dont_give_me_five(-4045, 2575))
print(dont_give_me_five(-5, 4))

"""
def jimmy_neutron(value):
    # print(n % 10)
    num = 0
    x = 0
    arr = [x := ((10 ** (sudo - 1)) + int(x) * 9) for sudo in range(0, len(str(value)))]
    for i in range(len(str(value)), 0, -1):
        if i >= 0 and (y := int(value % (10 ** (i + 1)) / 10 ** i)) != 0:
            num += arr[i] * y
            if y == 5:
                num += (value % (10 ** i))
                return num
            if y >= 5: num += 10 ** i - arr[i]
    return num


   for i, num in enumerate(string):
        x = ((10 ** (g))+ x * 9)
        if i > 1 and (y := (n % (10 ** (i + 1)) / 10 ** i)) != 0:
          if y == 5:
            x = (x * int(y)) + 1
    return x
# print(i, n)
# print(f"digit: {digit}")"""
