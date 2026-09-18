class Angajat:
    def __init__(self, nume, salariu):
        self.nume = nume
        self.salariu = salariu

    def afiseaza_info(self):
        print(f"Angajat: {self.nume}, Salariu: {self.salariu} euro")

    def mareste_salariu(self, procent):
        self.salariu += self.salariu * procent / 100


class Manager(Angajat):
    def __init__(self, nume, salariu, numar_subalterni):
        super().__init__(nume, salariu)
        self.numar_subalterni = numar_subalterni

    def afiseaza_info(self):
        print(
            f"Manager: {self.nume}, "
            f"Salariu: {self.salariu} euro, "
            f"Subalterni: {self.numar_subalterni}"
        )


angajat = Angajat("Ion", 4000)
manager = Manager("Maria", 7000, 12)

print("=== Informatii initiale ===")
angajat.afiseaza_info()
manager.afiseaza_info()

print("\n=== Dupa marirea salariului cu 10% ===")
angajat.mareste_salariu(10)
manager.mareste_salariu(10)

angajat.afiseaza_info()
manager.afiseaza_info()