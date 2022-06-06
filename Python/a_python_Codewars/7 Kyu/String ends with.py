def solution(string, ending):
    if len(ending) < 1:
        return True
    for i in range(len(ending)):
        if string[-(len(ending)):] == ending:
            return True
        else:
            return False