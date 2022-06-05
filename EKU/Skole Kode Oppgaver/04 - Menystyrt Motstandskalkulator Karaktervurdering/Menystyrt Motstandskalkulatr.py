lst = []
# lager tom liste for å fylle den opp med informasjon senere
# blir plassert utenfor while loop slik at det er en global variabel

serie_farge = "\033[31;1m"  # bright red
parallell_farge = "\033[34;1m"  # bright blue
fgBrightYellow = "\033[33;1m"  # bright yellow
normal = "\033[0m"  # tilbakestiller farge forandringer
# Dette er ASCI farge koder, her er link hvis du er interessert i å vite mer
# https://www.codegrepper.com/code-examples/actionscript/python+ascii+colors

def clear():
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')


def rp():
    """ resistor_type blir om til Serie eller Parallell basert på bruker input og vice versa
    rp() legger til "p" til Rtot slik at Rtot blir Rptot hvis det er Parallell"""
    if resistor_type == f"Parallell":
        return "p"
    else:
        return ""

def farge_bestemmer():
    if resistor_type == "Parallell":
        print("______________________________________\n"
                f"{parallell_farge}{resistor_type}kobling Motstandskalkulator{normal}"
                "\n______________________________________\n"
                f"{parallell_farge}Beregnet R{rp()}tot = {Sum:.2f} Ω{normal}")
    elif resistor_type == "Serie":
        print("______________________________________\n"
                f"{serie_farge}{resistor_type}kobling Motstandskalkulator{normal}"
                "\n______________________________________\n"
                f"{serie_farge}Beregnet R{rp()}tot = {Sum:.2f} Ω{normal}")


while True:
    try:
        lst.clear()
        # lst.clear() er en list method som tømmer listen for innhold
        # forhindrer tidligere bruker input fra å forstyrre ønsket framtidig beregninger
        mode = int(input("=------------------------------------------=\n"
                         f"{serie_farge}* Tast 1: Serie Motstands Kalkulator{normal}       =\n"
                         f"{parallell_farge}* Tast 2: Parallell Motstands Kalkulator{normal}   =\n"
                         "=------------------------------------------=\n"
                         f"** Tast inn {serie_farge}1{normal} eller {parallell_farge}2{normal}: "))
        clear()
        # clear funksjonen rydder opp i konsollen slik at det er plass for ny informasjon
        if (mode > 2) or (mode < 1):
            print(f"{serie_farge}VALUE ERROR! TALL SOM IKKE ER 1 ELLER 2{normal}\n"
                  f"Bare tast inn 1 eller 2 når du velger mellom {serie_farge}Serie{normal} og"
                  f"{parallell_farge}Parallell{normal} "
                  f"motstandskalkulator!"
                  f"\n{serie_farge}ERROR!{normal}"
                  "\n... RESTARTER LOOP!")
            continue
        antall_motstander = int(input(f"Tast inn antall motstander: "))
        for antall in range(0, antall_motstander) :
            Resistor = int(input(f"Tast inn R{antall + 1} Verdi: "))  # Bruker input som legger til Motstands verdier
            lst.append(Resistor)  # Legger Resistor til i en liste
    except ValueError:
        print(f"{serie_farge}ERROR! Ikke tast inn bokstaver!! Bare tall!{normal}")
        continue
    Sum = 0
    
    if mode == 1:
        resistor_type = "Serie"  # Lagrer Serie verdien i String for å bruke det til noe annet senere
        for antall in range(0, len(lst)):
            Sum += lst[antall]  # Regner ut Seriemotstander og lagrer den i Sum variabel
        farge_bestemmer()
    elif mode == 2:
        resistor_type = "Parallell"  # Lagrer Serie verdien i String for å bruke det til noe annet senere
        for antall in range(0, len(lst)):
            Sum += 1 / (lst[antall])  # Dette tilsvarer 1 / R1, R2, R3 osv i parallell formelen
        Sum = 1 / Sum  # ^ Dette er den ekstra !*eneren*! som deler på alt fra Sum, !*1*! / ( 1 / R1) + ( 1 / R2)
        clear()
        farge_bestemmer()
    slutt = input("\n\nTast inn hva som helst for å fortsette: ")
    if slutt is True:
        clear()
    #  Vennligst tast inn hvilken som helst knapp for å starte programmet om igjen
    #  Den er nødvendig for å vise rtot imens vi bruker clear funksjonen for å rydde opp konsollen
