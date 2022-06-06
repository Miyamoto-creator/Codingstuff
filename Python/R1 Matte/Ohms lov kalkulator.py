import sys


# Added func to the ends of the functions
# And changed variable names

def voltsfunc(i, r) :
    return i * r


def resistancefunc(v, i) :
    return v / i


def currentfunc(v, r) :
    return v / r


def wattagefunc(a, v) :
    return a * v


while True :
    decision = input("what do you want to find type help for commands  :")

    if (decision == "exit" or decision == "Exit") :
        sys.exit(0)

    if (decision == "help") :
        print("""Type "v" to find voltage""")
        print("""Type "i" to find current""")
        print("""Type "r" to find resistance""")
        print("""Type "w" to find wattage""")
        print("""Type "m" to find all possible outcomes""")

    if (decision == "v" or decision == "V") :
        currentin = float(input("What is the current  :"))
        resistancein = float(input("What is the resistance  :"))
        outputvolts = voltsfunc(currentin, resistancein)
        outputvolts = str(outputvolts)
        print("#######################")
        print(outputvolts + "volts")
        print("#######################")

    if (decision == "r" or decision == "R") :
        voltsin = float(input("What is the voltage  :"))
        currentin = float(input("What is the current  :"))
        outputresistance = resistancefunc(voltsin, currentin)
        outputresistance = str(outputresistance)
        print("###########################")
        print(outputresistance + "ohms")
        print("###########################")

    if (decision == "i" or decision == "I") :
        voltsin = float(input("What is the voltage  :"))
        resistancein = float(input("What is the resistance :"))
        outputcurrent = currentfunc(voltsin, resistancein)
        outputcurrent = str(outputcurrent)
        print("#######################")
        print(outputcurrent + "amps")
        print("#######################")

    if (decision == "w" or decision == "W") :
        currentin = float(input("What is the current  :"))
        voltsin = float(input("Waht is the voltage  :"))
        outputwattage = wattagefunc(currentin, voltsin)
        print("#######################")
        print(outputwattage + "watts")
        print("#######################")

    if (decision == "m" or decision == "M") :
        try :
            voltsin = float(input("What is the volts if you dont have it just press enter  :"))
        except ValueError :
            voltsin = ''
        try :
            currentin = float(input("What is the current if you dont have it just press enter  :"))
        except ValueError :
            currentin = ''
        try :
            resistancein = float(input("What is the resistance if you dont have it just press enter :"))
        except ValueError :
            resistancein = ''
        try :
            wattagein = float(input("What is the wattage  :"))
        except ValueError :
            wattagein = ''

        if (voltsin == '' and currentin == '' and resistancein == '') :
            print("Please type an amount for 2 fields")
        else :

            if (type(voltsin) == float and type(resistancein) == float and type(currentin) == str) :
                currentin = currentfunc(voltsin, resistancein)
                float(currentin)
            if (type(voltsin) == float and type(currentin) == float and type(resistancein) == str) :
                resistancein = resistancefunc(voltsin, currentin)
                float(resistancein)
            if (type(currentin) == float and type(resistancein) == float and type(voltsin) == str) :
                voltsin = voltsfunc(resistancein, currentin)
                float(voltsin)
            if (type(voltsin) == float and type(currentin) == float and type(wattagein) == str) :
                wattagein = wattagefunc(voltsin, currentin)
                float(wattagein)

            voltsin = str(voltsin)
            currentin = str(currentin)
            resistancein = str(resistancein)
            wattagein = str(wattagein)
            print("############################################")
            print("The voltage is " + voltsin + " volts")
            print("Current is " + currentin + " amps")
            print("The resistance is " + resistancein + " ohms")
            print("The wattage is " + wattagein + " watts")
            print("############################################")
