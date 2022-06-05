from random_tall import *
# fra random_tall python filen import * som betyr import alt som er i denne filen over hit.
# Du må ha random_tall og test bullshit i samme fil mappe for at dette skal virke
while True:
    print("W Loop 1")
    randlist.clear()
    # randlist.clear() er en list method som tømmer listen for innhold
    # https://www.geeksforgeeks.org/different-ways-to-clear-a-list-in-python/ hvis du vil lese deg mer opp på det
    # lurer på å lignende måter og manipulere lister så søker du "data type" og methods på google
    tilfeldige()
    while True:
        print("W Loop 2")
        try:
            meny = int(input("Print 0 to use break\n" "Number please: "))
        except:
            print("Something unexpected has happened")
            continue
            # uten continue så sitter denne fast på try og except, den virker ikke skikkelig uten
        if meny == 0:
            break
            # får deg fra å være fast i W Loop 2 til W Loop 1, som tømmer listen din også fyller den opp med en ny en
        elif meny == 1:
            printerb()
        elif meny == 2:
            sorterer()
        elif meny == 3:
            legg_til_tall()
        elif meny == 4:
            slette_ett_tall()
        elif meny == 5:
            antall_tall()
        elif meny == 6:
            gjennomsnittet()
        elif meny == 7:
            quit()
