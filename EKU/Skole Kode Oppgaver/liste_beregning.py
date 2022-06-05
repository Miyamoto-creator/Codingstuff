def kalkuler_sum(liste):
    total_sum = sum(liste)
    return total_sum

def skriv_ut_resultat(lokal_tabell, lokal_sum):
    print(lokal_tabell)
    print("total sum =", lokal_sum)

def les_inn_tall(antall = 4):
    tall_liste = []
    for i in range(antall):
        try:
            tall = int(input(f"Skriv inn tall {i + 1}: "))
            tall_liste.append(tall)
        except ValueError:
            print("ValueError ... Bzzttt, restarting!")
    return tall_liste