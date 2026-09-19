class Produs:
    def __init__(self, nume, pret, cantitate_stoc):
        self.nume = nume
        self.pret = pret
        self.cantitate_stoc = cantitate_stoc

    def valoare_totala_stoc(self):
        return self.pret * self.cantitate_stoc

    def __str__(self):
        return f"{self.nume} - {self.pret} euro - Stoc: {self.cantitate_stoc}"