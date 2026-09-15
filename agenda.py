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

        print("\n=== LISTA CONTACTELOR ===")

        for index, linie in enumerate(linii, start=1):
            nume, telefon = linie.strip().split(",")
            print(f"{index}. {nume} - {telefon}")

    except FileNotFoundError:
        print("Nu exista niciun contact salvat.")


def cauta_contact():
    nume_cautat = input("Nume de cautat: ").lower()

    try:
        with open("contacte.txt", "r") as fisier:
            linii = fisier.readlines()

    except FileNotFoundError:
        print("Nu exista niciun contact salvat.")
        return

    gasit = False

    for linie in linii:
        nume, telefon = linie.strip().split(",")

        if nume_cautat in nume.lower():
            print(f"Gasit: {nume} - {telefon}")
            gasit = True

    if not gasit:
        print("Niciun contact gasit cu acest nume.")


def sterge_contact():
    nume_de_sters = input("Nume contact de sters: ").lower()

    try:
        with open("contacte.txt", "r") as fisier:
            linii = fisier.readlines()

    except FileNotFoundError:
        print("Nu exista niciun contact salvat.")
        return

    linii_ramase = []
    gasit = False

    for linie in linii:
        nume, telefon = linie.strip().split(",")

        if nume.lower() == nume_de_sters:
            gasit = True
        else:
            linii_ramase.append(linie)

    if gasit:
        with open("contacte.txt", "w") as fisier:
            fisier.writelines(linii_ramase)

        print("Contactul a fost sters.")
    else:
        print("Nu am gasit un contact cu acest nume.")


while True:
    afiseaza_meniu()

    optiune = input("Alege o optiune (1-5): ")

    if optiune == "1":
        adauga_contact()

    elif optiune == "2":
        afiseaza_contacte()

    elif optiune == "3":
        cauta_contact()

    elif optiune == "4":
        sterge_contact()

    elif optiune == "5":
        print("La revedere!")
        break

    else:
        print("Optiune invalida, incearca din nou.")