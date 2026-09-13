def afiseaza_meniu():
    print("\n=== AGENDA DE CONTACTE ===")
    print("1. Adauga contact")
    print("2. Afiseaza toate contactele")
    print("3. Cauta contact")
    print("4. Sterge contact")
    print("5. Iesire")


while True:
    afiseaza_meniu()
    optiune = input("Alege o optiune (1-5): ")

    if optiune == "1":
        print("Aici vom adauga un contact")

    elif optiune == "2":
        print("Aici vom afisa contactele")

    elif optiune == "3":
        print("Aici vom cauta un contact")

    elif optiune == "4":
        print("Aici vom sterge un contact")

    elif optiune == "5":
        print("La revedere!")
        break

    else:
        print("Optiune invalida, incearca din nou.")