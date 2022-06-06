from math import factorial as fac
import numpy as np
from itertools import product, combinations


def tester(word):
    _, villemo = np.unique([i for i in word], return_counts=True)
    print(villemo)
    result = 0
    for j in range(len(word)):
        k = sum(1 for i in word[j + 1:] if i < word[j])
        result += k * fac(len(word) - j)
    sotra = ""
    for j in range(len(word)):
        for i in word[j]:
            sotra += i
        #print(sotra)
        a = set([i for i in combinations(word, j)])
        print(a)
    return result - 1

x = 0


print(tester('SUNIL'))
print("95 is the right answer for SUNIL")
print(tester('MISSISSIPPI'))
print("13737 is the right answer for MISSISSIPPI")
print(fac(4)*3 + fac(3)*3 + fac(2)*3)
#print(tester('sandeep'))


#     tren = [sub_permutations.index(i) for i in char]
# length = len(word) - 1
# letters = word
# tester = sorted(word)
# print(tester)
# first_letter = tester.index(word[0])
# sub_permutations = sorted(word)
# min_length = len(sub_permutations)
# alex = []
# tiles = {}
# for letter in letters:
#     tiles[letter] = tiles.get(letter, 0) + 1
# char, nums = list(tiles.keys()), list(tiles.values())
# total = 0

# for j in range(len(sub_permutations)):
#     for i, n in enumerate(tiles.keys()):
#             if len(alex) == 0:
#                 alex.append(n)
#                 total += fac(min_length) * first_letter
#             elif n in word[0] and n in sub_permutations:
#                 show = tiles_letters[j]
#                 tets = letters[i]
#                 alex += n
#                 sub_permutations.remove(n)

# def tester(word):
#     length = len(word) - 1
#     letters = word
#     tester = sorted(word)
#     print(tester)
#     first_letter = tester.index(word[0])
#     sub_permutations = sorted(word)
#     min_length = len(sub_permutations)
#     alex = []
#     tiles = {}
#     for letter in letters:
#         tiles[letter] = tiles.get(letter, 0) + 1
#     char, nums = list(tiles.keys()), list(tiles.values())
#     total = 0
#     tren = [sub_permutations.index(i) for i in char]
#     result = 0
#     for i, n in enumerate(tren):
#         if n == 0:
#            break
#         elif sum(nums) == len(word):
#             result += fac(n) * first_letter
#         else:
#             print("ready for missipi")
#     print(result)
#     #print(tren)
#     g = 0
#     tiles_letters = sorted(list(tiles.keys()))
#     return result - 1
