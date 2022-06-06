antall_motstander = []

def shortener():
    global x
    if mode == 1 :
        x = "Serie"
    elif mode == 2 :
        x = "Parallell"
    print("______________________________________\n"
          f"{x}kobling Motstandskalkulator"
          "\nVennligst tast inn dine 3 Motstands verdier"
          "\n______________________________________")

def serie():
  lst = []
  n = int(input("Enter Number of Resistors: "))
  for i in range(0, n):
      Resistor = int(input(f"Tast inn R{i+1}: "))
      lst.append(Resistor)
  print(lst)
  Sum = 0
  for antall in range(0, len(lst)):
    print(lst[antall], "Ω")
    Sum += lst[antall]
  print(f"Beregnet Rtot: {Sum} Ω")


def parallell():
    Sum = 0
    antall_motstander = []
    for antall in range(0, len(antall_motstander)):
        print(antall_motstander[antall], "Ω")
        Sum += 1 / (1 / antall_motstander[antall])
    return Sum

def input_resistor_list():
    Num = input("Input Resistor Value: ")
    if bool(Num) == False:
        return antall_motstander
    elif bool(Num) == True:
        try:
            Num = int(Num)
            antall_motstander.append(Num)
        except ValueError:
            print("Value Error")

def amount_of_resistors():
    Num = int(input("Input Amount of Resistors: "))
    Num += antall_motstander




while True:
    mode = int(input("______________________________________\n"
                     "Tast 1 for å velge SERIE MOTSTANDS KALKULATOR\n"
                     "Tast 2 for å velge Parallellkobling Motstands kalkulator"
                     "\n______________________________________\n"
                     "Tast inn ditt valg her: "))
    if mode == 1:


    elif mode == 2:
