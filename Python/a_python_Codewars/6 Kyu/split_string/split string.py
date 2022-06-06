def solution(s) :
    great = "-".join(s[i :i + 2] for i in range(0, len(s), 2))
    x = great.split("-")
    b = "_"
    index = len(s) - len(x)
    print(f"X is: {len(x)}, S is: {len(s)}, index is: {index}")
    if index % 2 == 0 :
        for i in range(0, index) :
            return print(x, "1")
        else :
            x[index] += b
            return print(x, "2")
    elif index > 2 :
        x[index] += b
        return print(x, "3")
    elif index == -1 :
        x = []
        return print(x, "4")


solution("asdfads")
solution("asdfadsf")
solution('x')
solution('')
