def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

parallell_farge = "\033[34;1m"  # bright blue
normal = "\033[0m"  # tilbakestiller farge forandringer

lst = []
kalkulator = (f"======================================\n"
      f"*      {parallell_farge}Parallell Motstands Kalkulator{normal}    *\n"
      f"======================================")
print(kalkulator)
antall_motstander = int(input(f"Tast inn antall motstander: "))
clear()
print(kalkulator)
for antall in range(0, antall_motstander):
    Resistor = int(input(f"Tast inn R{antall + 1} Verdi: "))
    lst.append(Resistor)
Sum = 0
antall_motstander = []

for antall in range(0, len(antall_motstander)):
    print(antall_motstander[antall], "Ω")
    Sum += antall_motstander[antall]

for antall in range(0, len(lst)):
    Sum += 1 / lst[antall]
Sum = 1 / Sum
clear()
print(kalkulator)
print(f"{parallell_farge}Rptot = {Sum:.2f}{normal}")