def dont_give_me_five(start, end):
    num = 0
    x = 0
    def kim(n):
        digit = 0
        effective_digit = 0
        x = 0
        while n > 0:
            for i, n in enumerate(str(n)):
                if int(n) % 10 == 0:
                    digit += 1
                    effective_digit = ((10 ** (i - 1)) + kim * 9)
                return effective_digit

    if (end >= 0 and start >= 0) or (end < 0 and start < 0):
        return kim(max(abs(end), abs(start))) - kim(min(abs(start), abs(end)) - 1)
    else:
        return kim(abs(end)) + kim(abs(start)) + 1




print(dont_give_me_five(-5000, 5000))


"""def dont_give_me_five(start, end):
    def give_me_five(value, x=1):
        print(len(str(value)))
        for i in range(0, len(str(value))):
            x = ((10 ** i) + x * 9)
            if i >= 1 and (y := (value % (10 ** (i + 1)) / 10 ** i)) != 0:
                x *= int(y)
        return x
    if (end >= 0 and start >= 0) or (end < 0 and start < 0):
        return give_me_five(value = max(abs(end), abs(start)) - min(abs(start), abs(end)))
    else:
        return give_me_five(value = max(abs(end), abs(start)) + min(abs(start), abs(end)))

print(dont_give_me_five(1, 1000))"""
