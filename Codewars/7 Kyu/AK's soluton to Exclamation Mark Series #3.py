def func(s="LCEMINUBMEANV!HXVVKG!!!"):
    c = 0
    s_reverse = s[::-1]
    print("IN: " + s)

    for index, char in enumerate(s_reverse):
        if char == "!":
            c += 1

        if char.isalpha():
            break

    s = s.replace("!", "") + "!" * c

    return print("OUT: " + s)