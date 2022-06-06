"""liste lage program"""
__version__ = "V1.2"
__author__ = "Kim-Robin"

import random

def manual():
    """setter sinskrivde verdier inn i en liste"""

    value_list = []

    while True:

        value = input(":")

        if bool(value) is False:  # skjekker om brukeren har skrivd inn noe

            return value_list

        elif bool(value) is True:

            try:  # skjekker om det er ett tall ellers prøver den på nytt

                value = int(value)
                value_list.append(value)

            except TypeError:
                continue


def randint(lenght=6,min_num=1,max_num=34):
    """generates int list of given lenght"""

    value_list = []
    while len(value_list) != lenght:
        fail = False
        num = random.randint(min_num, max_num)
        num = str(num)
        if len(num) < 2:
            num = "0" + num
        if len(value_list) != 0:
            for y in range(0, len(value_list)):
                if num != value_list[y]:
                    continue
                else:
                    fail = True
                    break
            if fail is False:
                value_list.append(num)
        else:
            value_list.append(num)

    return value_list


def randfloat(lenght=10):
    """generates random list of given length"""

    value_list = []
    for i in range(0, lenght):

        print(i)
        value_list.append(random.random(0, 1))

    return value_list
