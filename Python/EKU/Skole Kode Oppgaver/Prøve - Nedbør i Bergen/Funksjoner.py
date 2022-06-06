def kalkuler_sum(liste):
    total_sum = sum(liste)
    return total_sum

def skriv_ut_resultat(lokal_tabell, lokal_sum):
    print(lokal_tabell)
    print(f"Totalt Nedbør for 20. Oktober til 31 Oktober = {lokal_sum}")

def les_inn_tall():
    tall_liste = [56.9, 27.6, 8.8, 7.2, 2.2, 50.5, 10.5, 32.3, 26.0, 87.9, 10.6, 6.7]
    return tall_liste

def sorterer(sortert_sum):
    sortert_sum.sort(reverse=True)
    return print(f"C: Lag en subrutine som sorterer listen fra størst til minst: \n "
          f"{sortert_sum}")

def legg_til_tall(tall_liste):
    siste_tall = float(input("Legg till et tall sist i listen: "))
    tall_liste.append(siste_tall)
    return print(f"Lag en subrutine som legger til et tall sist i listen: \n "
          f"{tall_liste}")

def gjennomsnittet(tall_liste):
    gjennomsnitt = sum(tall_liste) / len(tall_liste)
    return print(f"Gjennomsnittet til Nedbør i Bergen er: {gjennomsnitt:.2f}")