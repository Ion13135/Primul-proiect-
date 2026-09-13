# Functia imparte

def imparte(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Eroare: impartire la zero"


# 2. Testarea functie

print(imparte(10, 2))
print(imparte(5, 0))
print(imparte(9, 3))


# 3 si 4. Citirea varstei cu validare

while True:
    try:
        varsta = int(input("Introdu varsta: "))

        if varsta < 0:
            print("Varsta nu poate fi negativa!")
            continue

        print("Multumesc!")
        break

    except ValueError:
        print("Te rog introdu un numar valid!")