import numpy as np
import matplotlib.pyplot as plt

dataset = [27.166,
           29.3951,
           30.4918,
           27.6947,
           30.6119,
           33.3482,
           33.3309,
           32.6508,
           34.6585,
           31.8127,
           31.8455,
           30.9567,
           31.9984,
           33.8698,
           32.3476,
           34.8577,
           33.2813,
           35.677,
           34.2351,
           35.098,
           33.54,
           34.468,
           36.008,
           37.914,
           38.522,
           41.594,
           41.756,
           41.885,
           42.646,
           42.171,
           43.537,
           42.623,
           44.012,
           44.357,
           43.382,
           43.972,
           45.714,
           44.837,
           43.268,
           45.697,
           44.817,
           44.342,
           44.639,
           45.078,
           45.616,
           44.8,
           44.372,
           44.469,
           42.865,
           41.283, ]
hst = []
lst = []
op = 0

for i in range(49):
    lst.append(dataset[i + 1] - dataset[i])
    h = (dataset[i + 1] - dataset[i])
    print(f"{i + 1}: {dataset[i + 1]} - {i}: {dataset[i]} = {h}")
for j in range(49):
    op += 1
    hst.append((lst[j]) / op)
    print(f"{op}: {((lst[j]) / op)}")
print(hst)

"""
def twoSum(self, nums: List[int], target: int):
  prevMap = {}  # val : index
  for i, n in enumerate(nums):
    diff = target - n
    print(f"iter_num: {i}")
    print(f"elem_num: {n}")
    if diff in prevMap:
      return f"{nums[prevMap[diff]]} + {nums[i]} {target}? True"
    prevMap[n] = i
    hore = ("False" if not diff == target else True)
    print(f"{nums[prevMap[n]]} + {nums[i]} = {diff} is {target}? {hore}")
  return"""
hasj = {}
for i, n in enumerate(hst):
    hasj[n] = i + 1
print(hasj)
y = hasj.values()
x = hasj.keys()

plt.plot(hst)
plt.show()
