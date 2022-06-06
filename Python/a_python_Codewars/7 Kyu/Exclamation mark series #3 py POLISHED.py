def remove(string):
    lst = string.split(" ")
    string = ''.join(lst)
    string_index = string.count("!") + string.count("Hi")
    solution = ""
    for i in range(string_index):
        solution += string[i]
    return print(solution)


remove("Hi!!!! Hi!!! !!!Hi!!!")
