 # Exerciutiul A

print("Tabla inmultirii cu 7:")

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# Exercitiul B

contor = 0

numar = int(input("Introdu un numar (0 pentru oprire): "))

while numar != 0:
    contor += 1
    numar = int(input("Introdu un numar (0 pentru oprire): "))

print("Ai introdus", contor, "numere.")