def count_bits(n):
    n = int(input("Enter a number: "))
    b = []
    while n > 0:
        d = n % 2
        b.append(d)
        n = n // 2
    b.reverse()
    print("Binary Equivalent is: ")
    for i in b:
        print(i, end="")
    return b
count_bits(n=1)
