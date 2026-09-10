def este_par(numar):
    return numar % 2 == 0


def calculeaza_pret_final(pret, discount=0):
    return pret - (pret * discount / 100)


def converteste_temperatura(grade, unitate):
    if unitate == "C":
        return grade * 9 / 5 + 32
    elif unitate == "F":
        return (grade - 32) * 5 / 9


# Testare functie este_par
print(este_par(4))
print(este_par(7))

# Testare functie calculeaza_pret_final
print(calculeaza_pret_final(100, 20))
print(calculeaza_pret_final(50))

# Testare functie converteste_temperatura
print(converteste_temperatura(0, "C"))
print(converteste_temperatura(32, "F"))