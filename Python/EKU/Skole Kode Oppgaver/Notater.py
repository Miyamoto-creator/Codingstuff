import liste_beregning as lb

# Hovedprogram
#tallrekke = [2, 21, 89, 176]
tallrekke = lb.les_inn_tall(2)
hoved_sum = lb.kalkuler_sum(tallrekke)
lb.skriv_ut_resultat(tallrekke, hoved_sum)