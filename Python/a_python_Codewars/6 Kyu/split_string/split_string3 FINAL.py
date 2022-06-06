def solution(string):
    length = len(string)
    #parse to make even
    if length % 2 != 0:
        string = string + "_"
    #split into pairs
    completed_list = []
    for c in range(0, length, 2):
        completed_list.append(string[c] + string[c+1])
    return completed_list
