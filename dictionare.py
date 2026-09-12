# 1. Creează dicționarul student

student = {
    "nume": "Alex",
    "varsta": 18,
    "note": [8, 7, 10, 9]
}

# 2. Afișează numele și vârsta folosind .get()

print("Nume:", student.get("nume"))
print("Varsta:", student.get("varsta"))

# 3. Calculează media notelor

media = sum(student["note"]) / len(student["note"])
print("Media notelor:", media)

# 4. Funcție pentru adăugarea unei note

def adauga_nota(student, nota_noua):
    student["note"].append(nota_noua)
    print("Lista actualizata de note:", student["note"])

# Apelarea funcției
adauga_nota(student, 8)

# 5. Tuple cu data nașterii

nastere = (15, 6, 2005)

zi, luna, an = nastere

print("Ziua:", zi)
print("Luna:", luna)
print("Anul:", an)