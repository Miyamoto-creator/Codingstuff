def likes(lst):
    if len(lst) >= 3:
        half = [f"{lst[i]}, " for i in range(2, len(lst))]
        if len(half) > 1:
            return f"{lst[0]}, {lst[1]} and {len(half)} others like this"
        else:
            return f"{lst[0]}, {lst[1]} and {lst[2]} like this"

    elif len(lst) == 2:
        return "".join(f"{lst[0]} and {lst[1]} like this")

    elif len(lst) == 1:
        return f"{lst[0]} likes this"

    elif len(lst) == 0:
        return 'no one likes this'