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


if __name__ == "__main__":
    # Cream magazinul
    magazin = Magazin()

    # Cream produsele
    produs1 = Produs("Laptop", 3000, 5)
    produs2 = Produs("Mouse", 80, 20)
    produs3 = Produs("Tastatura", 250, 10)

    # Adaugam produsele
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