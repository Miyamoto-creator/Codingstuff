number, word = int(input()), input()  # more efficient way to add input

if number != 1:  # != instead of == so that 0 doesn't add plural
    word += 's'  # if number is NOT EQUAL to 1 then add 'S'
else:
    pass  # pass loop and go directly to print if number is not equal to 1
print(number, word)
