class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ele = [i for i in s]
        print(ele)
        unique = []
        target = 0
        for i, n in enumerate(ele):
            if n is target and not ele[i] == ele[i-1]:
                ele.insert(i, "!")
            if ele[i] == ele[i-1]:
                ele.insert(i, "!")
                target = n
        return ele
so = Solution()
print(so.lengthOfLongestSubstring("pwwkew"))