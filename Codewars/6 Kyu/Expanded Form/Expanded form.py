def expanded_form(num) :
    pass
    print(num)
    string = str(num)
    length = len(string)
    great = "-".join(string[i :i + 1] for i in range(length))
    solution = great.split("-")
    alexander = []
    for i, length in enumerate(solution) :
        alexander.append((string[-i - 1]))
        # print(string[-i-1])
    "".join(alexander)
    answer = int()
    for i in range(len(alexander)) :
        alexander[i] = int(alexander[i])

    complete_lst = []
    for j in range(len(alexander)) :
        alexander[j] = alexander[j] * 10 ** j
        complete_lst.append(alexander[j])
        print(alexander[j])
        print(j)
        print(complete_lst)
    for i in range(len(complete_lst)) :
        complete_lst[i] = str(complete_lst[i])

    #solution = complete_lst.split("+ 0")
    complete_lst.reverse()
    x = complete_lst.copy()
    print(f"string: {string}, solution is: {solution}, length is: {length}\n len_alex is: {len(alexander)}")
    for word in (range(len(x))):
        if "0" in x:
            x.remove("0")
        elif "+ 0" in x:
            x.remove(+ 0)
        else:
            return " + ".join(x)
        print(x)
