from itertools import permutations as perm

def permutations(string):
    return list("".join(i) for i in set(perm(string)))

print(permutations('aabb'))
