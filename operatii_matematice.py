def este_par(numar):
    return numar % 2 == 0


def calculeaza_pret_final(pret_initial, reducere_procent):
    return pret_initial - (pret_initial * reducere_procent / 100)


def converteste_temperatura(celsius):
    return celsius * 9 / 5 + 32