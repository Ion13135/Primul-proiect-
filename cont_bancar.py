class ContBancar:
    def __init__(self, titular, sold_initial=0):
        self.titular = titular
        self.sold = sold_initial
        self.istoric = []

    def depune(self, suma):
        self.sold += suma
        self.istoric.append(f"Depunere: +{suma}")

    def retrage(self, suma):
        if suma > self.sold:
            print("Fonduri insuficiente!")
        else:
            self.sold -= suma
            self.istoric.append(f"Retragere: -{suma}")

    def afiseaza_sold(self):
        print(f"Sold curent pentru {self.titular}: {self.sold} lei")


cont = ContBancar("Ion", 200)

cont.depune(100)
cont.afiseaza_sold()

cont.retrage(50)
cont.afiseaza_sold()

cont.retrage(500)
cont.afiseaza_sold()

cont.depune(20)
cont.afiseaza_sold()

print(cont.istoric)