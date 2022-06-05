

lst = []
Sum = 0

def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def shortener() :
    global x
    if mode == 1 :
        x = "Serie"
    elif mode == 2 :
        x = "Parallell"
    print("______________________________________\n"
          f"{x}kobling Motstandskalkulator"
          "\nHvor mange motstandsverdier vil du måle i dag?"
          "\n______________________________________")

def serie():
  lst = []
  Sum = 0
  n = int(input("Enter Number of Resistors: "))
  for i in range(0, n):
      clear()
      Resistor = int(input(f"Tast inn R{i+1}: "))
      lst.append(Resistor)
  print(lst)
  for antall in range(0, len(lst)):
    print(lst[antall], "Ω")
    Sum += lst[antall]
    clear()
  print(f"______________________________________\n")
  print(f"\033[2;31;40mBeregnet Rstot = {Sum:.2f} Ω"f"\033[1;39;49m")


def parallell():
  lst = []
  Sum = 0
  n = int(input("Enter Number of Resistors: "))
  for i in range(0, n):
      Resistor = int(input(f"Tast inn R{i+1}: "))
      lst.append(Resistor)
  print(lst)
  for antall in range(0, len(lst)):
    print(lst[antall], "Ω")
    Sum = 1 / lst[antall]
    Sum += Sum
    Sum = 1 / (Sum)
  print(f"______________________________________\n")
  print(f"\033[2;31;40mBeregnet Rptot = {Sum:.2f} Ω"f"\033[1;39;49m")


again = 0
while again < 10 :
    mode = int(input("______________________________________\n"
                     "Tast 1 for å velge SERIE MOTSTANDS KALKULATOR\n"
                     "Tast 2 for å velge Parallellkobling Motstands kalkulator"
                     "\n______________________________________\n"
                     "Tast inn ditt valg her: "))
    if mode == 1:
        clear()
        shortener()
        serie()
        again -= 1
    elif mode == 2 :
        shortener()
        parallell()
        again -= 1
    again += 1
