# 1 si 2. Nume complet + split

nume_complet = input("Introdu numele si prenumele: ")

nume, prenume = nume_complet.split()

print("Nume:", nume.capitalize())
print("Prenume:", prenume.capitalize())


# 3. Funtie pentru numararea vocalelor

def numara_vocale(text):
    vocale = "aeiou"
    contor = 0

    for litera in text.lower():
        if litera in vocale:
            contor += 1

    return contor


text = input("Introdu un text: ")
print("Numar de vocale:", numara_vocale(text))


# 4. Verificare email

email = input("Introdu adresa de email: ")

if "@" in email and email.endswith(".com"):
    print("Email valid")
else:
    print("Email invalid")


# 5- Join

cuvinte = ["Bine", "ai", "venit", "la", "Python"]

mesaj = "-".join(cuvinte)

print(mesaj)