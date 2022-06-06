import Funksjoner as fr

while True:
    tallrekke = fr.les_inn_tall()
    hoved_sum = fr.kalkuler_sum(tallrekke)
    try:
        meny = int(input("=-------------------------------------------------------------------=\n"
                         "* Tast 0: For å avslutte programmet                                 =\n"
                         "* Tast 1: Beregn og skriv ut total nedbør fra perioden              =\n"
                         "* Tast 2: Skriv ut nedbørstallene i minkende rekkefølge             =\n"
                         "* Tast 3: Beregn og skriv ut gjennomsittlig nedbør i denne perioden =\n"
                         "* Tast 4: Legg til nedbør for neste døgn i listen                   =\n"
                         "=-------------------------------------------------------------------=\n"
                         " ** Tast inn ditt valg her: "))
        print("=--------------------------------------------------------------------------------=")
    except:
        print("ERROR! Enter a number from 0 to 4, not a letter or anything else")
        continue
        
    if meny == 0:
        quit()
    elif meny == 1:
        fr.skriv_ut_resultat(tallrekke, hoved_sum)
    elif meny == 2:
        fr.sorterer(tallrekke)
    elif meny == 3:
        fr.gjennomsnittet(tallrekke)
    elif meny == 4:
        fr.legg_til_tall(tallrekke)
