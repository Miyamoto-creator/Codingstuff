"""Menystyrt resistor kaluulator basert på Curses"""
__version__ = "V1.1"
__author__ = "Kim-Robin"

import curses
import meny
import random
import string
from datetime import date

stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.keypad(True)
stdscr.nodelay(True)
RUNNING = True
POS = 0

#define colors
curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_CYAN)
curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_BLUE)
curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_WHITE)

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


def do_func(value):
    """Menu item selection function."""
    global RUNNING
    if value == 0:
        value_list = []
        num = meny.do_input("int",4,2)
        try:
            int(num)
        except ValueError:
            meny.do_error("No value Given",6,3)
            return
        date_today = date.today()
        price = num * 5
        price = f"KR {price}.00"
        if len(price) != 9:
            if len(price) != 8:
                price += "  "
            else:
                price += " "


        lotto = [
        "                                                  ",
        "   |X| LOTTO                                      ",
        "   -------------------------------------------    ",
        "   Spillkvitering                                 ",
        "                                                  ",
        f"   Dato:          {date_today}                      ",
        f"   Spilldato:     {date_today}                      ",
        "   Spilltype:     Enkle rekker                    ",
        "   Kupongtype:    KUP096                          ",
        "   Antall uker:   1                               ",
        f"   Referansenr:   {random.randint(100000,999999)}/{random.randint(1000,9999)}                     ",
        f"   Id-nummer:     { ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))}                      ",
        "   -------------------------------------------    ",
        "   UREGISTRERT SPILLER                            ",
        f"   Pris:       {price}                          ",
        "   -------------------------------------------    "
        ]
        lotto_two = [
        "   -------------------------------------------    ",
        "                                                  ",
        "             " + str("  ".join(randint(4,1000,9999)))+"               ",
        "                                                  "
        ]
        for i in range(0,num):
            temp_list = randint(7)
            temp_list.sort()
            if len(str(i+1)) < 2:
                lotto_num = " "+ str(i+1)
            else:
                lotto_num = str(i+1)
            num_string = f"           {lotto_num}. "+ " ".join(temp_list)+"               "
            value_list.append(num_string)

        print_list = []
        print_list.extend(lotto)
        print_list.extend(value_list)
        print_list.extend(lotto_two)
        meny.draw_text_box(3,1,40,print_list,0,54)
    if value == 1:
        RUNNING = False

menu = [
    "|New Numbers |",
    "|Exit        |",
]
choises = None
stdscr.bkgd(' ', curses.color_pair(0) | curses.A_BOLD)
value_list = []

while RUNNING:
    y ,x = stdscr.getmaxyx()
    KEY ,POS = meny.draw_menu(0,1,1,POS,menu,choises,10,30)
    meny.draw_tool_bar(2,["Lotto Generator",value_list,"Menu Item: " + str(POS),"Made By: Kim-Robin","","Version: 2.1"],2)
    stdscr.refresh()

    if KEY == 10:
        do_func(POS)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()
