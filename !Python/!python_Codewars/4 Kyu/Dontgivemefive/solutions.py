def dont_give_me_five(start, end):
    num = 0
    int_lst = []
    x = 0
    for i in range(start, end):
        if i % 10 == 0:
            x += 1
        int_lst.append(i)
        if "5" not in str(i):
            num += 1

    def kim(n):
        digit, kim = 1, 0
        while digit < len(str(end)):
            kim = ((10 ** (i - 1)) + kim * 9)
            digit += 1

    print(int_lst)
    if (end >= 0 and start >= 0) or (end < 0 and start < 0):
        kim(value = max(abs(end), abs(start)) - min(abs(start), abs(end)))
    else:
        kim(value = max(abs(end), abs(start)) + min(abs(start), abs(end)))

    print("value:", value)
    print("antall tiere i tallet:", x)
    print("Kim: ", kim)
    return print("num: ", abs(end) - abs(num))


dont_give_me_five(-10000, 1000)

""""10 for hver 50 til 59 i 100

# dette gjøres med å telle antall siffer i slutt tallet som om det var en tekst string også deretter gjøre len(string)



for hver ti har du en garantert femmer"""

print(21515142292 % 10)