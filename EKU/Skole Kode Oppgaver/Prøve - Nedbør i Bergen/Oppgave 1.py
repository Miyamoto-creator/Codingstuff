def les_inn_tall():
    tall_liste = [56.9, 27.6, 8.8, 7.2, 2.2, 50.5, 10.5, 32.3, 26.0, 87.9, 10.6, 6.7]
    return tall_liste

def kalkuler_sum(liste):
    total_sum = sum(liste)
    return print(f"Totalt Nedbør for 20. Oktober til 31 Oktober = {total_sum}")

tallrekke = les_inn_tall()
hoved_sum = kalkuler_sum(tallrekke)