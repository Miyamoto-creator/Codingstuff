def make_readable(seconds):
    I = seconds
    print(I)
    if I % (60*60) == 0:
        H = I // (60*60)
        M = 0
        S = 0
    else:
        H = I // (60*60)
        I = I % (60*60)
    if I % 60 == 0:
        M = I // 60
        S = 0
    else:
        M = I // 60
        S = I % 60
    H = str(H)
    M = str(M)
    S = str(S)
    if len(H) < 2:
        H = ("0" + H)
    if len(M) <  2:
        M = ("0" + M)
    if len(S) <  2:
        S = ("0" + S)
    return print(f"{H}:{M}:{S}")

make_readable(86399)
make_readable(359999)
