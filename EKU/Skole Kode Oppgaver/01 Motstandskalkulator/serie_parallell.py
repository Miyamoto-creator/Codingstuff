def serie_motstander():
    Sum = 0
    antall_motstander = []
    for antall in range(0, len(antall_motstander)):
        print(antall_motstander[antall], "Ω")
        Sum += antall_motstander[antall]
    return Sum


def parallell_motstander():
    Sum = 0
    antall_motstander = []
    for antall in range(0, len(antall_motstander)):
        print(antall_motstander[antall], "Ω")
        Sum /= 1/(antall_motstander[antall])
    return Sum
