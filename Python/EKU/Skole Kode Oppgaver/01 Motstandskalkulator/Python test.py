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
    Sum += 1 / (1 / lst[antall])
  print(f"Beregnet Rtot: {Sum} Ω")

serie()
