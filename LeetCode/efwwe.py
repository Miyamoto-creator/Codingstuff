import numpy as np
import timeit as t

class Solution:
    def __init(self, n, k):
        self.n = n
        self.k = k
    def getSmallestString(self, n, k):
        alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
        list_string = [0] * n
        reference = n
        Num = k
        for i in range(n):
            for j in range(len(alphabet)):
                stringValue = (ord(alphabet[~j]) - 96)
                if Num >= stringValue:
                    list_string[i] = stringValue
                    Num = Num - stringValue
                    reference -= 1
                    break
        not_zero = [i for i in list_string if np.all(i)]
        zero = list_string.count(0)
        one = list_string.count(1)
        if zero > 0:
            list_string[len(not_zero) - 1 - one] -= zero
            for i in range(len(not_zero), len(not_zero) + zero):
                list_string[i] = 1
        return "".join(sorted(sorted([chr(i + 96) for i in list_string]), key=str.upper)), list_string

"""
if zero > 0:
if len(list_string) - zero < 1:
list_string[abs(len(list_string) - zero)] -= zero
for i in range(len(not_zero), len(not_zero) + zero):
list_string[i] = 1
else:
list_string[len(list_string) - zero] -= zero
for i in range(len(not_zero), len(not_zero) + zero):
list_string[i] = 1"""
so = Solution()


print("Actual output: ",so.getSmallestString(n=67, k=882))
print("Expected output: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaapzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", ([ord(i)-96 for i in "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaapzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"]))
print("Run time:", t.timeit(lambda: so.getSmallestString(n=67, k=882), number=10000))

print("Actual output: ",so.getSmallestString(n=3, k=27))
print("Expected output: aay", ([ord(i)-96 for i in "aay"]))
print("Run time:", t.timeit(lambda: so.getSmallestString(n=3, k=27), number=10000))

print("Actual output: ",so.getSmallestString(n=2, k=18))
print("Expected output: aq", ([ord(i)-96 for i in "aq"]))
print("Run time:", t.timeit(lambda: so.getSmallestString(n=2, k=18), number=10000))

print("Actual output: ",so.getSmallestString(n=5, k=130))
print("Expected output: zzzzz", ([ord(i)-96 for i in "zzzzz"]))
print("Run time:", t.timeit(lambda: so.getSmallestString(n=5, k=130), number=10000))

print("Actual output: ",so.getSmallestString(n=4, k=63))
print("Expected output: ajzz", ([ord(i)-96 for i in "ajzz"]))
print("Run time:", t.timeit(lambda: so.getSmallestString(n=4, k=63), number=10000))

print("Actual output: ",so.getSmallestString(n=4, k=100))
print("Expected output: vzzz", ([ord(i)-96 for i in "vzzz"]))
print("Run time:", t.timeit(lambda: so.getSmallestString(n=4, k=100), number=10000))

print("Actual output: ",so.getSmallestString(n=5, k=73))
print("Expected output: aaszz", ([ord(i)-96 for i in "aaszz"]))
print("Run time:", t.timeit(lambda: so.getSmallestString(n=5, k=73), number=10000))


"""q = __import__("functools").partial(__import__("os")._exit, 0)  # FIXME
__import__("IPython").embed()  # FIXME"""

"""def coinChange(totalNumber, coins):

    coins = [0] * coins
    N = totalNumber

    index = len(coins) - 1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue:
            index -= 1

        if N == 0:
            break



print(coinChange(27, 3))"""