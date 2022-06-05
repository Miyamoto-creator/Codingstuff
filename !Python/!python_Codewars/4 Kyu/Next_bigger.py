from itertools import permutations as perm
import timeit as t

def next_bigger(n):
    first_lst = ["".join(i) for i in sorted(perm(str(n)), reverse=True)]
    big = int(first_lst[first_lst.index(str(n))-1])
    return big if big > n else -1

print("Run time 1:", t.timeit(lambda: next_bigger(n=12345678910111213141516171819202122232425), number=10000))



#print("Run time 2:", t.timeit(lambda: nxt(n=20170), number=10000))



print(next_bigger(10))