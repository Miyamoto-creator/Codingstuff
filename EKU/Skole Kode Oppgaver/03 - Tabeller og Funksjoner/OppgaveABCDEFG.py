def rand_nums():
    import random
    randlist = []
    for num in range(10):
        randlist.append(random.randint(0, 99))
    print(randlist)
    print(f"Oppgave 1 A og B: Lag kode som leser inn 10 tilfeldige tall inn i en tabell og skriver ut listen"
          f": \n "
          f"{randlist}")
    randlist.sort(reverse=True)
    print(f"Oppgave 1 C: Lag en subrutine som sorterer listen fra størst til minst: \n "
          f"{randlist}")
    print(f"Oppgave 1 D: Lag en subrutine som legger til et tall sist i listen: \n "
          f"{randlist}")
    siste_tall = int(input("Legg till et tall sist i listen: "))
    randlist.append(siste_tall)

    print(f"Oppgave 1 E: Lag en subrutine som lar deg slette ett ønsket tall fra listen: \n "
          f"{randlist}")
    slett_tall = int(input("Skriv inn tallet som du ønsker å slette fra listen: "))
    randlist.remove(slett_tall)
    print(f'Printer liste uten {slett_tall}:\n'
          f' {randlist}')
    print(f"Oppgave 1 F: Lag en subrutine som skrivet ut antall tall i listen: \n "
          f"{len(randlist)}")
    print(f"Oppgave 1 G: Lag en subrutine som beregner gjennomsnitet av tallene i listene: \n "
          f"{randlist}")
    gjennomsnitt = sum(randlist) / len(randlist)
    print(f"Gjennomsnittet til Randlist er: {gjennomsnitt}")
    return randlist

