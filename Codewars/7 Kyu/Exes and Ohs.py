def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# MY SOLUTION <
def xo(s):
    s = s.lower()
    x = s.count('x')
    o = s.count('o')
    if (x == o):
        return True
    elif 'x' and 'o' == 0:
        return True
    else:
        return False

https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

Smarter Solutions:

def xo(s):
    return s.lower().count('x') == s.lower().count('o')