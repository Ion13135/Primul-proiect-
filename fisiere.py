# 1. Functia care salveaza un contact

def salveaza_contact(nume, telefon):
    with open("contacte.txt", "a") as fisier:
        fisier.write(f"{nume} - {telefon}\n")


# 2. Adaugare a 3 cntacte

salveaza_contact("Ion", "0712345678")
salveaza_contact("Maria", "0723456789")
salveaza_contact("Vasile", "0734567890")


# 3. Functia care afiseaza contactele

def afiseaza_contacte():
    with open("contacte.txt", "r") as fisier:
        for numar, linie in enumerate(fisier, start=1):
            print(f"{numar}. {linie.strip()}")


print("Lista contactelor:")
afiseaza_contacte()


# 4. Citirea unui fisier inexistent

try:
    with open("nu_exista.txt", "r") as fisier:
        print(fisier.read())
except FileNotFoundError:
    print("Fisierul nu a fost gasit!")