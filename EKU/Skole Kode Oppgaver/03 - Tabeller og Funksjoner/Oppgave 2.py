from random_tall import *

again = 0
while again < 10:
    tilfeldige()
    print("W Loop 1")
    while True:
        print("W Loop 2")
        try:
            meny = int(input("=-----------------------------------------------------=\n"
                             "* Tast 1: Skrive ut listen                            =\n"
                             "* Tast 2: Sortere listen fra størst til minst         =\n"
                             "* Tast 3: Legger til et tall sist i listen\           =\n"
                             "* Tast 4: Slette ett ønsket tall fra listen           =\n"
                             "* Tast 5: Skriver ut antall tall i listen             =\n"
                             "* Tast 6: Beregner gjennomsnittet av tallene i listen =\n"
                             "=-----------------------------------------------------=\n"
                             " ** Tast inn ditt valg her: "))
            print("=--------------------------------------------------------------------------------=")
        except:
            print("ERROR! Enter a number from 1 to 6, not a letter or anything else")
        if meny == 1:
            printerb()
            again -= 1
        elif meny == 2:
            sorterer()
            again -= 1
        elif meny == 3 :
            legg_til_tall()
            again -= 1
        elif meny == 4:
            slette_ett_tall()
            again -= 1
        elif meny == 5:
            antall_tall()
            again -= 1
        elif meny == 6:
            gjennomsnittet()
            again -= 1
        elif meny == 8:
            break
    print("again plus 1")
    again += 1
