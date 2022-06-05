import re

def dont_give_me_five(start, end):
        def goo(n):
                result = 0
                pos9 = 1
                while n > 0:
                    digit = n % 10
                    effective_digit = digit
                    if digit > 5:
                        effective_digit -= 1
                    to_add = effective_digit * pos9
                    if digit == 5:
                        result = -1
                    result += to_add
                    n //= 10
                    pos9 *= 9
                return result

def regex_divisible_by(n):
    preList = []
    postList = []
    s = ""
    if n == 1:
        return re.sub(r'^(0|1)+$', '10', n)
    elif n >= 13 and n == 10:
        return re.sub(r'[0*1*]*[1*0*]*', '10', re.sub('^(0|1)+$', '10', str(n)))


print(regex_divisible_by(2))
"""
def kebabize(s):
    return re.sub('\B([A-Z])', r'-\1', re.sub('\d', '', s)).lower()
    
    def regex_divisible_by(n):
    if n != 1:
        return re.sub(r'[0*1*]*[1*0*]*', '10', str(n))
    return re.sub('^(0|1)+$', '10', str(n))"""