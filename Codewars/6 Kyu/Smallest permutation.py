from itertools import permutations as perm

def min_permutation(n):
    if str(n)[0] == '-':
        string, minus = str(n).replace('-', ''), True
    else:
        string, minus = str(n), False
    lst = []
    for i, j in enumerate(set(sorted(perm(string)))):
        if j[0] == '0':
            continue
        else:
            lst.append("".join(j))
    return '-' + min(lst) if minus else min(lst)

print(min_permutation(29394))