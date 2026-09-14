def afiseaza_meniu():
    print("\n=== AGENDA DE CONTACTE ===")
    print("1. Adauga contact")
    print("2. Afiseaza toate contactele")
    print("3. Cauta contact")
    print("4. Sterge contact")
    print("5. Iesire")


def adauga_contact():
    nume = input("Nume contact: ")
    telefon = input("Telefon: ")

    with open("contacte.txt", "a") as fisier:
        fisier.write(f"{nume},{telefon}\n")

    print(f"Contactul {nume} a fost adaugat!")


def afiseaza_contacte():
    try:
        with open("contacte.txt", "r") as fisier:
            linii = fisier.readlines()

        if not linii:
            print("Nu exista niciun contact salvat.")
            return

        for index, linie in enumerate(linii, start=1):
            nume, telefon = linie.strip().split(",")
            print(f"{index}. {nume} - {telefon}")

    except FileNotFoundError:
        print("Nu exista niciun contact salvat.")


while True:
    afiseaza_meniu()
    optiune = input("Alege o optiune (1-5): ")

    if optiune == "1":
        adauga_contact()

    elif optiune == "2":
        afiseaza_contacte()

    elif optiune == "3":
        print("Aici vom cauta un contact")

    elif optiune == "4":
        print("Aici vom sterge un contact")

    elif optiune == "5":
        print("La revedere!")
        break

    else:
        print("Optiune invalida, incearca din nou.")