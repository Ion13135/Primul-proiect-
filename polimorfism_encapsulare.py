class FormaGeometrica:
    def calculeaza_arie(self):
        pass


class Dreptunghi(FormaGeometrica):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def calculeaza_arie(self):
        return self.lungime * self.latime


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.raza = raza

    def calculeaza_arie(self):
        return 3.14159 * self.raza ** 2


forme = [
    Dreptunghi(5, 3),
    Cerc(2),
    Dreptunghi(10, 4)
]

print("=== POLIMORFISM ===")

for forma in forme:
    print(f"Aria: {forma.calculeaza_arie()}")


class ContSecurizat:
    def __init__(self, pin, sold):
        self.__pin = pin
        self.__sold = sold

    def verifica_sold(self, pin_introdus):
        if pin_introdus == self.__pin:
            return self.__sold
        else:
            return "PIN incorect!"


print("\n=== ENCAPSULARE ===")

cont = ContSecurizat("1234", 5000)

print(cont.verifica_sold("1234"))
print(cont.verifica_sold("9999"))