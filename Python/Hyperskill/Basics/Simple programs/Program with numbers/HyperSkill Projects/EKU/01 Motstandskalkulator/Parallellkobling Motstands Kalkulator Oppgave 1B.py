print("______________________________________\n"
      "Parallellkobling Motstandskalkulator"
      "\n______________________________________\n"
      "Vennligst tast inn dine 3 Motstands verdier"
      "\n______________________________________")

R1, R2, R3 = float(input("Tast inn R1: ")), float(input("Tast inn R2: ")), float(input("Tast inn R3: "))
R_tot = 1/(1 / R1 + 1 / R2 + 1 / R3)
print(f"______________________________________\n"
      f"Beregnet Rtot = {R_tot:.2f} Ω")
