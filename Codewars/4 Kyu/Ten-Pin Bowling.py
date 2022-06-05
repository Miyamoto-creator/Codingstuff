import re

def bowling_score(frames):
    arr = [i for i in "".join(frames.split())]
    X_LIST = [i for i, j in enumerate(arr) if j == 'X']
    SPARE = [i for i, j in enumerate(arr) if j == '/']
    for i in X_LIST:
        print(arr[i+1], arr[i+2])

    return SPARE, X_LIST


#print(f"{bowling_score('11 11 11 11 11 11 11 11 11 11')} should equal 20")
#print(f"{bowling_score('X X X X X X X X X XXX')} should equal 300")
#print(f"{bowling_score('X 11 X 11 X 11 X 11 X XXX')} should equal 116")
print(f"{bowling_score('X 1/ 5 11 X 11 X 11 X 11')} should equal 84")
#
# print(20 + 20 + 20 + 20 + 20 + 20 + 20 + 20 + 20 + 20 + 40 + 60)
# print(20 + 20 + 20 + 20 + 20 + 20 + 20 + 20 + 20 + 120)
# print(20 * 7 + 20 * 3 * 3)

"""def find_x(x):
        if 'X' in string:
            string.replace('X', 10)
    if not 'X' or '/' or 'X' and '/' in string:
        return sum([int(i[0]) + int(i[1]) for i in string])"""

# print(len(n))
# print(money)
# string = []
# for i in frames:
#     if i != ' ':
#         string += "".join(i)
#     elif i == 'X':
#         string += "".join(i + 'X')
# string = list(zip(string[::2], string[1::2]))
# string = [(i) for i in string]
# treas = 0
# for iter, ele in enumerate(string):
#     pass
    # treas += int(float(ele[0])) + int(float(ele[1]))

#
# def bowling_score(frames):
#     print(frames)
#     def strike_sum(x):
#         result = []
#         for iteration in range(x):
#             result.append(20 * (iteration + 1))
#             #result.append(10 + 10 * tall_delt_på_10 * (iteration + 1))
#         return sum(result)
#     bowling = [re.sub('([X])+', '20' * len(i), i) for n, i in enumerate(frames.split(' ', 10))]
#     print("bowling",bowling)
#     bowler = list(zip(bowling[::2], bowling[0:9:]))
#     #bowler = sum([map(int, i + j) for i, j in bowling[0:9]])
#     result = 0
#     for i, j in bowling[0:9]:
#         result += int(i) + int(j)
#     last = tuple([i for i in bowling[9]])
#     end = (list(zip(last[0:len(last):2], last[1:len(last):2])))
#     tissefant = [i + j for i, j in end]
#     store = 0
#     for i, j in enumerate(tissefant):
#         store += int(j) * (i + 1)
#     print("store: ",store)
#
#     print("pisser ut av tissefanten 1:", tissefant)
#     kuk = [i + j for i, j in (list(zip(last[0:len(last):2], last[1:len(last):2])))]
#     print("pisser ut av kuken 2: ", kuk)
#     score = []
#     for strike in bowling:
#         if strike.count('20') > 0:
#             score.append(strike_sum(strike.count('20')))
#     money = 0
#     for i, n in enumerate(bowling):
#         if not n == '20':
#             money += int(n)
#     return sum(score) + result