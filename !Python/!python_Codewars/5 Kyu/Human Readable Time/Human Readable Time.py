def make_readable(seconds) :
    I = seconds
    if I % 3600 == 0 :
        H = I // (60 * 60)
        M = 0
        S = 0
    else :
        H = I // 3600
        I = I % 3600
    if I % 60 == 0 :
        M = I // 60
        S = 0
    else :
        M = I // 60
        S = I % 60
    if len(str(H)) > 2 :
        str(H) +=
    return print(f"{H}:{M}:{S}")

make_readable(60)
