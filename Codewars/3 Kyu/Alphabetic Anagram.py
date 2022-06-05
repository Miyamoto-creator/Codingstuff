import timeit as t
from operator import itemgetter
import numpy as np
from itertools import permutations as perm, islice, combinations_with_replacement




def listPosition(word):
    return ["".join(i) for i in sorted(set(perm(word)))].index(word) + 1

print(listPosition('QUESTION'))
# print(listPosition('MISSISSIPPI'))
# print("Run time:", t.timeit(lambda: listPosition(word='MISSISSIPPI'), number=10000))
# print(listPosition('QUESTION'))
# print("Run time:", t.timeit(lambda: listPosition(word='QUESTION'), number=10000))
print(listPosition('BOOKKEEPER'))
# print("Run time:", t.timeit(lambda: listPosition(word='BOOKKEEPER'), number=10000))
# print(listPosition('WORD'))
# print("Run time:", t.timeit(lambda: listPosition(word='WORD'), number=10000))
# print(listPosition('ABAB'))
# print("Run time:", t.timeit(lambda: listPosition(word='ABAB'), number=10000))
# print(listPosition('AAAB'))
# print("Run time:", t.timeit(lambda: listPosition(word='AAAB'), number=10000))


# def listPosition(word):
#     test = "".join([str(ord(i)) for i in word])
#     print(len(test))
#     return ["".join(i) for i in sorted(set(((perm(test)))), key=str)]
