# Sistem de Gestiune Magazin


O aplicație CLI (Command Line Interface) dezvoltată în Python pentru gestionarea produselor unui magazin. Aplicația permite administrarea stocurilor, vânzarea produselor și salvarea automată a datelor în fișiere pentru utilizare între sesiuni.

---

## Functionalitati

- Adăugare produse noi în magazin
- Afișare listă produse disponibile
- Căutare produse după nume
- Vânzare produse cu verificarea stocului disponibil
- Actualizare automată a stocului după vânzare
- Salvare produse în fișier text
- Încărcare automată a produselor la pornirea aplicației
- Prevenirea adăugării produselor duplicate
- Meniu interactiv în consolă

---

## Concepte OOP folosite

### Clase și Obiecte
- Clasa `Produs` reprezintă un produs individual.
- Clasa `Magazin` gestionează toate produsele magazinului.

### Compoziție
- Clasa `Magazin` conține o listă de obiecte `Produs`.

### Metode de instanță
- Fiecare obiect are propriile date și comportamente prin metode.

### Încapsulare
- Datele unui produs sunt organizate și gestionate prin intermediul obiectelor.

### Metode speciale
- Metoda `__init__()` pentru inițializarea obiectelor.
- Metoda `__str__()` pentru afișarea prietenoasă a produselor.

### Reutilizarea codului
- Metoda `cauta_produs()` este reutilizată de alte funcționalități precum vânzarea produselor.

---

## Tehnologii folosite

- Python 3
- Programare Orientată pe Obiecte (OOP)
- Fișiere text (.txt)
- Gestionarea excepțiilor (`try/except`)
- PyCharm
- Git & GitHub

---

## Structura proiectului

```text
magazin-cli/
│
├── produs.py
├── magazin.py
├── produse.txt
└── README.md
```

---

## Cum se ruleaza

Asigură-te că Python este instalat pe sistem.

```bash
python magazin.py
```

---

## Exemplu de utilizare

```text
=== MAGAZIN ===
1. Adauga produs
2. Afiseaza produse
3. Vinde produs
4. Salveaza in fisier
5. Iesire

Alege o optiune (1-5): 1

Nume produs: Monitor
Pret: 350
Cantitate stoc: 8

Produsul 'Monitor' a fost adaugat in magazin.
```

### Exemplu de vânzare

```text
Alege o optiune (1-5): 3

Nume produs de vandut: Monitor
Cantitate: 3

Vandut: 3 x Monitor = 1050.0 euro.
Stoc ramas: 5
```

---

## Salvarea datelor

Produsele sunt salvate într-un fișier text:

```text
Monitor,350.0,5
Laptop,3000.0,3
Mouse,80.0,20
```

La următoarea pornire a aplicației, produsele sunt încărcate automat din acest fișier.

---

## Validari implementate

- Nu se pot adăuga produse duplicate.
- Nu se poate vinde un produs inexistent.
- Nu se poate vinde o cantitate mai mare decât stocul disponibil.
- Sunt tratate erorile de introducere a prețului și cantității.
- Gestionarea situației în care fișierul de produse nu există.

---

## Ce am invatat

Prin dezvoltarea acestui proiect am învățat să:

- Construiesc aplicații folosind Programarea Orientată pe Obiecte.
- Lucrez cu mai multe module Python.
- Organizez codul într-o structură clară și reutilizabilă.
- Gestionez colecții de obiecte.
- Salvez și încarc date din fișiere text.
- Implementez validări și tratarea excepțiilor.
- Creez aplicații CLI interactive.
- Dezvolt proiecte complete, documentate și pregătite pentru GitHub.

---

## Autor

**Ion Sobraneschi**

Junior Python Developer & Data Analyst Enthusiast