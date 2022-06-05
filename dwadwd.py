from math import factorial

def lexicographic_index(p):
    result = 0
    for j in range(len(p)):
        k = sum(1 for i in p[j + 1:] if i < p[j])
        result += k * factorial(len(p) - j)
    return result

def lexicographic_followers(p):
    return factorial(len(p)) - lexicographic_index(p) - 1

print(lexicographic_followers("QUESTION"))