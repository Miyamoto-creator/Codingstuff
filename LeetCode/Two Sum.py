"""https://leetcode.com/problems/two-sum/
https://www.youtube.com/watch?v=KLlXCFG5TnA"""
from typing import List


class Solution:
    def init(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self, nums: List[int], target: int):
        prevMap = {}  # val : index
        for i, n in enumerate(nums): # for iteration, number in list of numbers
            diff = target - n # calculate difference between target and each number element
            if diff in prevMap: # do not reuse the same element to achieve target number
                return f"{nums[prevMap[diff]]} + {nums[i]} = {target}?"
                #return [prevMap[diff], i]
            prevMap[n] = i
        return

class Solution:
    def init(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self, nums: List[int], target: int):
        prevMap = {}  # val : index
        for i, n in enumerate(nums):
          diff = target - n
          print(f"iter_num: {i}")
          print(f"elem_num: {n}")
          if diff in prevMap:
            return f"{nums[prevMap[diff]]} + {nums[i]} {target}? True"
            #return [prevMap[diff], i]
          prevMap[n] = i
          hore = ("False" if not diff == target else True)
          print(f"{nums[prevMap[n]]} + {nums[i]} = {diff} is {target}? {hore}")
        return


La = Solution()
La.nums = [2, 3, 4, 7]
La.target = 6
print(La.twoSum([2, 3, 4, 7], 6))
print(La.twoSum([10, 90, 70, 30], 100))


La = Solution()
La.nums = [2, 3, 4, 7]
La.target = 6
print(La.twoSum([2, 3, 4, 7], 6))
print(La.twoSum([10, 90, 70, 30], 100))
