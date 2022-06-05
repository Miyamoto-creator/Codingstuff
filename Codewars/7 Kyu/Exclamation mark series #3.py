import re

def remove(string):
    last_letter = (re.findall('[a-zA-Z]', string)[-1])
    last_exclamation = (re.findall('[!]', string)[-1])
    print(last_letter)
    print(last_exclamation)
    #results = [(i.start(), i.end(), i.group()), for i in re.finditer(r"abc", x)][-1]
    f_results = [i for i in re.findall('[a-zA-Z]', string)]
    print(f_results, "f results")
    exclamation_mark = ""
    for i in string:
        if not i.isalpha():
            exclamation_mark += i

    lst = string.split()
    print(lst[-1])



    # Counts total amount of string length
    length = len(string)

    # Indexes position of each Hi to get their indices
    counter = -1
    text = ""
    for x in string:
        counter += 1
        print(x, counter)
        if x.isalpha():
            text += x
        elif not x.isalpha():
            exclamation_mark += x
    last_exclamation = (exclamation_mark[-1])
    last_letter = (text[-1])
    last_number = string.rfind(last_exclamation) - string.rfind(last_letter)
    print(last_number)
    print("Last Letter Number:", string.rfind(last_letter), "\nLast Letter:", string[len(last_letter)])
    print("Last Exclamation Mark Number:", string.rfind(last_exclamation), "\nLength of String:", length - 1)
    for x in string:
        if "!":
            string = string.replace("!", "")
    return print(string + "!" * last_number)


remove('LCEMINUBMEANV!HXVVKG!!!')
