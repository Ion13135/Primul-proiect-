from produs import Produs


class Magazin:
    def __init__(self):
        self.produse = []

    def adauga_produs(self, produs):
        self.produse.append(produs)
        print(f"Produsul '{produs.nume}' a fost adaugat in magazin.")

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
                f"Stoc insuficient! Disponibil: {produs.cantitate_stoc}, "
                f"cerut: {cantitate}"
            )
            return None

        produs.cantitate_stoc -= cantitate

        total = produs.pret * cantitate

        print(
            f"Vandut: {cantitate} x {produs.nume} = "
            f"{total} euro. Stoc ramas: {produs.cantitate_stoc}"
        )

        return total


if __name__ == "__main__":
    magazin = Magazin()

    produs1 = Produs("Laptop", 3000, 5)
    produs2 = Produs("Mouse", 80, 20)
    produs3 = Produs("Tastatura", 250, 10)

    magazin.adauga_produs(produs1)
    magazin.adauga_produs(produs2)
    magazin.adauga_produs(produs3)

    print("\n=== TOATE PRODUSELE ===")
    magazin.afiseaza_produse()

    print("\n=== CAUTARE PRODUS EXISTENT ===")
    rezultat = magazin.cauta_produs("laptop")
    print(rezultat)

    print("\n=== CAUTARE PRODUS INEXISTENT ===")
    rezultat = magazin.cauta_produs("Monitor")
    print(rezultat)

    print("\n=== VANZARE REUSITA ===")
    magazin.vinde_produs("Laptop", 2)

    print("\n=== STOC INSUFICIENT ===")
    magazin.vinde_produs("Tastatura", 100)

    print("\n=== PRODUS INEXISTENT ===")
    magazin.vinde_produs("Monitor", 1)

    print("\n=== STOC FINAL ===")
    magazin.afiseaza_produse()