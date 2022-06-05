import re

"""
input 3, 27
output aay
"""
string = ''

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
list_nums = [(ord(i) - 96) for i in alphabet]
combined = dict(zip(alphabet, list_nums))


def func(n, k):
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    list_nums = [(ord(i) - 96) for i in reversed(alphabet)]
    length = {0} * n
    x = [list_nums[-1], list_nums[-1], list_nums[-1]]
    return x

def twoSum(nums, target):
    prevMap = {}  # val : index
    for i, n in enumerate(nums): # for iteration, number in list of numbers
        diff = target - n # calculate difference between target and each number element
        if diff in prevMap: # do not reuse the same element to achieve target number
            return f"{nums[prevMap[diff]]} + {nums[i]} = {target}?"
            #return [prevMap[diff], i]
        prevMap[n] = i
    return

print(func(3, 27))

""" def twoSum(self, nums: List[int], target: int):
        prevMap = {}  # val : index
        for i, n in enumerate(nums): # for iteration, number in list of numbers
            diff = target - n # calculate difference between target and each number element
            if diff in prevMap: # do not reuse the same element to achieve target number
                return f"{nums[prevMap[diff]]} + {nums[i]} = {target}?"
                #return [prevMap[diff], i]
            prevMap[n] = i
        return

while not len(prevMap) == num:
    for i, n in enumerate(reversed(alphabet)):
        diff = k - (ord(n) - 96)
        if diff in prevMap:
            result.append(prevMap[diff])
            if len(result) == 3:
                return result
        prevMap[i] = (ord(n) - 96)
    print(prevMap)
print(len(prevMap))"""


def converter(s):
    value = []
    for i in string:
        value.append(ord(i) - 96)
    return value


s = "yaa"


def lexico(s):
    return sorted(sorted(s), key=str.upper)


print(lexico(s))


def twoSum(n, k):
    lst = [0 for i in range(n)]
    prevMap = {}  # val : index
    for i, ele in enumerate(lst):  # for iteration, number in list of numbers
        diff = k - ele  # calculate difference between target and each number element
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[ele] = i
    return


# print(twoSum(3, 27))
"""


def jimmy_neutron(start, end):
    count = lambda n: int(re.sub(r'5(\d*)', lambda m: '4' + '9' * len(m[1]), str(n)).translate(str.maketrans("56789", "45678")), 9)
    if start > 0:
        return count(end) - count(start - 1)
    elif end < 0:
        return count(-start) - count(-end - 1)
    else:
        return count(end) + count(-start) + 1"""
