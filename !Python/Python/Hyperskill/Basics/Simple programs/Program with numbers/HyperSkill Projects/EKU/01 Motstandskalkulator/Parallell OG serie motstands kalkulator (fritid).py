def shortener():
    global x
    if mode == 1:
        x = "Serie"
    elif mode == 2:
        x = "Parallell"
    print("______________________________________\n"
          f"{x}kobling Motstandskalkulator"
          "\nVennligst tast inn dine 3 Motstands verdier"
          "\n______________________________________")


again = 0
while again < 10:
    mode = int(input("______________________________________\n"
                     "Tast 1 for å velge SERIE MOTSTANDS KALKULATOR\n"
                     "Tast 2 for å velge Parallellkobling Motstands kalkulator"
                     "\n______________________________________\n"
                     "Tast inn ditt valg her: "))
    if mode == 1:
        shortener()
        R1, R2, R3 = float(input("Tast inn R1: ")), float(input("Tast inn R2: ")), float(input("Tast inn R3: "))
        Rs_tot = R1 + R2 + R3
        print(f"______________________________________\n")
        print(f"\033[2;31;40mBeregnet Rstot = {Rs_tot:.2f} Ω"f"\033[1;39;49m")
        again -= 1
    elif mode == 2:
        shortener()
        R1, R2, R3 = float(input("Tast inn R1: ")), float(input("Tast inn R2: ")), float(input("Tast inn R3: "))
        Rp_tot = 1 / (1 / R1 + 1 / R2 + 1 / R3)
        print(f"______________________________________\n")
        print(f"\033[2;31;40mBeregnet Rptot = {Rp_tot:.2f} Ω"f"\033[1;39;49m")
        again -= 1
    again += 1
