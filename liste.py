# 1. Lista cu 5 note
note = [8, 6, 10, 4, 7]

# 2. Suma si media notelor
suma_note = sum(note)
media_note = suma_note / len(note)

print("Suma notelor:", suma_note)
print("Media notelor:", media_note)

# 3 Nota maxima si minima
print("Nota maxima:", max(note))
print("Nota minima:", min(note))


# 4. Functie care numara notele de trecere
def numara_note_de_trecere(note):
    contor = 0

    for nota  in note:
        if nota >= 5:
            contor += 1

    return contor


print("Numar note de trecere:", numara_note_de_trecere(note))


# 5. Afisarea notelor cu numerate()
for index, nota in enumerate(note):
    print(f"{index + 1}: {nota}")