skudd_år = []                               # Lager skudd_års liste for å lagre skudd år i senere.
vanlig_år = []                              # Lager vanlig_års liste for å lagre vanlige år i senere.

for år in range(1600, 2000):                # Kjører 400 iterasjoner som starter på 1600 og slutter på 2000.
    if år % 400 == 0:                       # Det er ikke skuddår med mindre iterasjon er delelige med 400, SJEKKER FØRST!
        print(f'{år} er et skuddår')
        skudd_år.append(år)                 # Legger iterasjon til i skudd_år liste.
    elif år % 4 == 0 and not år % 100 == 0: # Sjekker om iterasjon IKKE er delelige med 100
                                            # før den sjekker om den er delelige med 4
        print(f'{år} er et skuddår')
        skudd_år.append(år)                 # Legger iterasjon til i skudd_år liste.
    else:                                   # Alt annet som faller utenfor sjekkene faller innenfor dette området.
        vanlig_år.append(år)                # Legger iterasjon til i Vanlig_år liste.
        print(f'{år} er ikke et skuddår')
print("vanlig år:", vanlig_år, "\n \n Skudd år:", skudd_år,
      f"\n Lengde av skudd års liste: {len(skudd_år)}") # <--- len(skudd_år)
"""Sjekker lengde av skudd års liste, hvert 400nde år så skal det være 97 år totalt.
Så dette programmet virker helt perfekt for dette scenarioet."""
