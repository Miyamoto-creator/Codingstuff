"""Main menu for list program / Main loop."""
__version__ = "V1"
__author__ = "Kim-Robin"

import curses
from curses.textpad import Textbox

stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()

def add_box(y_width=30,x_width=5,y_pos=1,x_pos=1,color_pair=0):
    """ Makes a window with assigned name and pos/size"""
    winname = curses.newwin(y_width,x_width,y_pos,x_pos)
    winname.keypad(True)
    winname.nodelay(True)
    winname.bkgd(' ', curses.color_pair(color_pair) | curses.A_BOLD)
    return winname


def get_key(window=stdscr):
    """increments/decrements the menu position."""
    key = window.getch()
    return key

def get_max(window=stdscr):
    return window.getmaxyx()

def draw_menu(color,y_pos, x_pos, current_pos, text=None,window=stdscr,y_width=0, x_width=0,horisontal=False):
    """Draws the basic menu screen."""
    key = stdscr.getch()
    if window != stdscr:
        window = curses.newwin(y_width,x_width,y_pos,x_pos)
        window.bkgd(' ', curses.color_pair(color) | curses.A_BOLD)
    window.erase()
    if horisontal:
        if key in (454, 258):
            current_pos += 1
            if current_pos >= len(text):
                current_pos = 0
        if key in (452, 259):
            current_pos -= 1
            if current_pos <= -1:
                current_pos = len(text)-1
        y, x = window.getmaxyx()

        width = int(x / len(text)-1)
        form_text = ""
        for i in range(0,len(text)):
            form_text = "|" + text[i]
            while len(form_text) < width-1:
                form_text += " "
            form_text += "|"

            if current_pos == i:
                window.addstr(0, width * i+1, str(form_text), curses.A_REVERSE)
            else:
                window.addstr(0, width * i+1, str(form_text))
        window.refresh()
        return (key,current_pos)

    else:
        if key in (456, 258):
            current_pos += 1
            if current_pos >= len(text):
                current_pos = 0
        if key in (450, 259):
            current_pos -= 1
            if current_pos <= -1:
                current_pos = len(text)-1

        for i in range(0,len(text)):
            if current_pos == i:
                window.addstr(y_pos+i, x_pos, str(text[i]), curses.A_REVERSE)
            else:
                window.addstr(y_pos+i, x_pos, str(text[i]))
        window.refresh()
        return (key,current_pos)

def draw_tool_bar(mode ,values=[],color=1):
    """Draws a blue bar at the top of the screen with array info and other stuff."""
    y, x = stdscr.getmaxyx()
    if mode == 0:
        top_tool_bar = curses.newwin(1, 0)
        top_tool_bar.clear()
        top_tool_bar.bkgd(' ', curses.color_pair(color) | curses.A_BOLD)
        top_tool_bar.addstr(0, 1, str(values[0]))
        top_tool_bar.addstr(0, int(x/2-(len(str(values[1]))/2)), str(values[1]))
        top_tool_bar.addstr(0, int(x-len(str(values[2]))-1), str(values[2]))
        top_tool_bar.refresh()
    if mode == 1:
        bottom_tool_bar = curses.newwin(1,0,y-1, 0)
        bottom_tool_bar.clear()
        bottom_tool_bar.bkgd(' ', curses.color_pair(color) | curses.A_BOLD)
        bottom_tool_bar.addstr(0, 1, str(values[0]))
        bottom_tool_bar.addstr(0, int(x/2-(len(str(values[1]))/2)), str(values[1]))
        bottom_tool_bar.addstr(0, int(x-len(str(values[2]))-1), str(values[2]))
        bottom_tool_bar.refresh()
    if mode == 2:
        top_tool_bar = curses.newwin(1, 0)
        top_tool_bar.clear()
        top_tool_bar.bkgd(' ', curses.color_pair(color) | curses.A_BOLD)
        top_tool_bar.addstr(0, 1, str(values[0]))
        top_tool_bar.addstr(0, int(x/2-(len(str(values[1]))/2)), str(values[1]))
        top_tool_bar.addstr(0, int(x-len(str(values[2]))-1), str(values[2]))
        top_tool_bar.refresh()

        bottom_tool_bar = curses.newwin(1,0,y-1, 0)
        bottom_tool_bar.clear()
        bottom_tool_bar.bkgd(' ', curses.color_pair(color) | curses.A_BOLD)
        bottom_tool_bar.addstr(0, 1, str(values[3]))
        bottom_tool_bar.addstr(0, int(x/2-(len(str(values[4]))/2)), str(values[4]))
        bottom_tool_bar.addstr(0, int(x-len(str(values[5]))-1), str(values[5]))
        bottom_tool_bar.refresh()


def do_input(value_type="string",y_pos=1,x_pos=1): 
    """Stuff."""
    message = ""
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    done = False
    while not done:
        #creates the text box windwo and typing window
        editwin = curses.newwin(1,20, y_pos+2,x_pos+8)
        inputwin = curses.newwin(5,36,y_pos,x_pos)
        editwin.clear()
        inputwin.clear()

        # sets upp det looks for the window
        inputwin.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
        inputwin.border()
        inputwin.addstr(1, 11, "Type value here", curses.A_BOLD)
        inputwin.addstr(3, 8, "Press Ctrl+G to quit", curses.A_BOLD)
        box = Textbox(editwin)
        inputwin.refresh()

        # Let the user edit until Ctrl-G is struck.
        box.edit()

        # Get resulting contents
        message = box.gather()

        if value_type == "int" and bool(message) is True:
            try:
                message = int(message)
            except ValueError:
                do_error("Recived non integear value",y_pos,x_pos)
                continue
        # Remooves the text box
        editwin.clear()
        inputwin.clear()
        inputwin.bkgd(' ', curses.color_pair(0) | curses.A_BOLD)
        inputwin.refresh()
        editwin.refresh()
        del editwin
        del inputwin
        done = True
    return message

def do_error(string,y_pos,x_pos):

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLUE)
    errorwin = curses.newwin(6,36,y_pos,x_pos)
    errorwin.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    while True:

        errorwin.border()
        errorwin.addstr(1, 14, "ERROR", curses.color_pair(2))
        errorwin.addstr(3, 2, string)
        errorwin.refresh()

        errorwin.nodelay(True)
        key = errorwin.getch()
        if key==10:
            break

    errorwin.bkgd(' ', curses.color_pair(0) | curses.A_BOLD)
    errorwin.clear()
    errorwin.refresh()
    del errorwin


def do_popup(string, y_pos=1, x_pos=1,name="Info!"):

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    popwin = curses.newwin(6, 36, y_pos, x_pos)
    popwin.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    while True:

        popwin.border()
        popwin.addstr(2, 20, name, curses.color_pair(0))
        popwin.addstr(3, 3, string)
        popwin.refresh()

        popwin.nodelay(False)
        key = popwin.getch()
        if key == 10:
            break

    popwin.bkgd(' ', curses.color_pair(0) | curses.A_BOLD)
    popwin.clear()
    popwin.refresh()
    del popwin

def draw_text_box(color,y_pos,x_pos,text,y_width = 0,x_width = 0):
    y,x = get_max()
    if y_width < len(text) + 2: y_width = y - (y_pos*2)
    window = curses.newwin(y_width, x_width, y_pos, x_pos)
    window.clear()
    window.border()
    window.refresh()
    for i in range(0,len(text)):
        window.addstr(i+1, 2, str(text[i]), curses.color_pair(color))
        window.refresh()
        

curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()