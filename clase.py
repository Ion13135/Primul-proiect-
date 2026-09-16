class Carte:
    def __init__(self, titlu, autor, an_publicare):
        self.titlu = titlu
        self.autor = autor
        self.an_publicare = an_publicare

    def afiseaza_info(self):
        print(f"Cartea '{self.titlu}' de {self.autor}, publicata in {self.an_publicare}")

    def este_veche(self):
        return self.an_publicare < 1990


carte1 = Carte("Ion", "Liviu Rebreanu", 1920)
carte2 = Carte("Harry Potter", "J.K. Rowling", 1997)
carte3 = Carte("1984", "George Orwell", 1949)

carte1.afiseaza_info()
print(carte1.este_veche())

carte2.afiseaza_info()
print(carte2.este_veche())

carte3.afiseaza_info()
print(carte3.este_veche())