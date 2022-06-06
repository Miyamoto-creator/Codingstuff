import timeit as t

class Solution:
    def getSmallestString(self, n, k):
        Amount = k - n
        Change = [1] * n
        index = 26
        counter = n - 1
        while True:
            if Amount >= (index - 1):
                Change[counter] += index - 1
                Amount -= index - 1
                counter -= 1
                continue
            elif Amount == 0:
                break
            index -= 1
        return "".join([chr(i + 96) for i in Change])

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