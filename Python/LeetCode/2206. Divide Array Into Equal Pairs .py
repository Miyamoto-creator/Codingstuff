from collections import Counter
import numpy as np


class Solution:
    def divideArray(self, nums):
        values = Counter(nums)
        x = [i for i in values.values()]
        return True if sum(x) % 2 == 0 else False




so = Solution()
print(so.divideArray([3,2,3,2,2,2]))

""""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

"""
