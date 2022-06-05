def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

serie_farge = "\033[31;1m"  # bright red
normal = "\033[0m"  # tilbakestiller farge forandringer

lst = []
kalkulator = (f"======================================\n"
      f"*      {serie_farge}Serie Motstands Kalkulator{normal}    *\n"
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
    Sum += lst[antall]
clear()
print(kalkulator)
print(f"{serie_farge}Rtot = {Sum}{normal}")
