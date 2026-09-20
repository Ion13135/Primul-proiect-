from produs import Produs


class Magazin:
    def __init__(self):
        self.produse = []

    def adauga_produs(self, produs):
        existent = self.cauta_produs(produs.nume)

        if existent is not None:
            print(
                f"Produsul '{produs.nume}' exista deja! "
                f"Foloseste alt nume."
            )
            return

        self.produse.append(produs)

        print(
            f"Produsul '{produs.nume}' a fost adaugat in magazin."
        )

    def afiseaza_produse(self):
        if not self.produse:
            print("Magazinul nu are niciun produs.")
            return

        for index, produs in enumerate(self.produse, start=1):
            print(f"{index}. {produs}")

    def cauta_produs(self, nume_cautat):
        for produs in self.produse:
            if produs.nume.lower() == nume_cautat.lower():
                return produs

        return None

    def vinde_produs(self, nume_produs, cantitate):
        produs = self.cauta_produs(nume_produs)

        if produs is None:
            print(f"Produsul '{nume_produs}' nu exista in magazin.")
            return None

        if cantitate > produs.cantitate_stoc:
            print(
                f"Stoc insuficient! Disponibil: "
                f"{produs.cantitate_stoc}, cerut: {cantitate}"
            )
            return None

        produs.cantitate_stoc -= cantitate

        total = produs.pret * cantitate

        print(
            f"Vandut: {cantitate} x {produs.nume} = "
            f"{total} euro. "
            f"Stoc ramas: {produs.cantitate_stoc}"
        )

        return total

    def salveaza_in_fisier(self, nume_fisier="produse.txt"):
        with open(nume_fisier, "w") as fisier:
            for produs in self.produse:
                fisier.write(
                    f"{produs.nume},{produs.pret},{produs.cantitate_stoc}\n"
                )

        print(f"Produsele au fost salvate in {nume_fisier}.")

    def incarca_din_fisier(self, nume_fisier="produse.txt"):
        try:
            with open(nume_fisier, "r") as fisier:
                self.produse = []

                for linie in fisier:
                    nume, pret, cantitate = linie.strip().split(",")

                    produs = Produs(
                        nume,
                        float(pret),
                        int(cantitate)
                    )

                    self.produse.append(produs)

            print(f"Produsele au fost incarcate din {nume_fisier}.")

        except FileNotFoundError:
            print(f"Fisierul {nume_fisier} nu exista inca.")


def afiseaza_meniu():
    print("\n=== MAGAZIN ===")
    print("1. Adauga produs")
    print("2. Afiseaza produse")
    print("3. Vinde produs")
    print("4. Salveaza in fisier")
    print("5. Iesire")


if __name__ == "__main__":
    magazin = Magazin()

    magazin.incarca_din_fisier()

    while True:
        afiseaza_meniu()

        optiune = input("Alege o optiune (1-5): ")

        if optiune == "1":
            nume = input("Nume produs: ")

            try:
                pret = float(input("Pret: "))
                cantitate = int(input("Cantitate stoc: "))

                produs_nou = Produs(
                    nume,
                    pret,
                    cantitate
                )

                magazin.adauga_produs(produs_nou)

            except ValueError:
                print("Pret sau cantitate invalida!")

        elif optiune == "2":
            magazin.afiseaza_produse()

        elif optiune == "3":
            nume = input("Nume produs de vandut: ")

            try:
                cantitate = int(input("Cantitate: "))
                magazin.vinde_produs(nume, cantitate)

            except ValueError:
                print("Cantitate invalida!")

        elif optiune == "4":
            magazin.salveaza_in_fisier()

        elif optiune == "5":
            magazin.salveaza_in_fisier()
            print("La revedere!")
            break

        else:
            print("Optiune invalida.")