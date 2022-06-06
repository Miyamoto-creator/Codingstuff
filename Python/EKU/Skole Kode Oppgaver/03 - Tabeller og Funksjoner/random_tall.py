import random
randlist = []

def tilfeldige():
    for num in range(10):
        randlist.append(random.randint(0, 99))
    return print(randlist)

def printerb():
    return print(f"B - Lag subrutine for å skrive ut listen: \n "
    f"{randlist}")

def sorterer():
    randlist.sort(reverse=True)
    return print(f"C: Lag en subrutine som sorterer listen fra størst til minst: \n "
          f"{randlist}")

def legg_til_tall():
    siste_tall = int(input("Legg till et tall sist i listen: "))
    randlist.append(siste_tall)
    return print(f"D: Lag en subrutine som legger til et tall sist i listen: \n "
          f"{randlist}")

def slette_ett_tall():
    slett_tall = int(input("Skriv inn tallet som du ønsker å slette fra listen: "))
    randlist.remove(slett_tall)
    return print(f"E: Lag en subrutine som lar deg slette ett ønsket tall fra listen: \n"
          f"{randlist}")

def antall_tall():
    return print(f"F: Lag en subrutine som skriver ut antall tall i listen\n"
          f"Antall tall i listen er: {len(randlist)}")

def gjennomsnittet():
    gjennomsnitt = sum(randlist) / len(randlist)
    return print(f"Gjennomsnittet til Randlist er: {gjennomsnitt}")
