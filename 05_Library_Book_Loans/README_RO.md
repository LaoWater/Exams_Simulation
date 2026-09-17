# Examen 5: Împrumuturi la bibliotecă

## Povestea
Săptămâna lecturii începe mâine, iar biblioteca școlii are nevoie de un program simplu pentru cărțile împrumutate. Membrii obișnuiți au o limită de împrumut. Elevii pot împrumuta trei cărți, însă nu pot lua acasă cărți din categoria `"reference"`.

Completează cele șase TODO-uri numerotate din `main.py`. Clasele, obiectele pentru exemple și un exemplu de rulare sunt oferite. Nu ai nevoie de input(), fișiere externe, pachete sau meniu.

## Format
- Timp orientativ: 90–120 de minute.
- Concepte: atribute, moștenire, `super()`, liste, condiții și bucle simple.
- Lucrează doar în `main.py`. Bonusul este separat de sarcinile principale.
- Presupune că primești obiecte Book valide, numere pozitive de pagini și limite de împrumut nenegative. Același membru nu va încerca să împrumute de două ori simultan aceeași carte. Nu trebuie să gestionezi un inventar global al bibliotecii.

## Sarcini principale
1. **`LibraryMember.can_borrow()`** — returnează dacă numărul de cărți împrumutate este strict mai mic decât `max_books`.
2. **`LibraryMember.borrow_book(book)`** — dacă există loc, adaugă cartea în listă și returnează `True`. Altfel returnează `False`, fără să modifici lista.
3. **`LibraryMember.return_book(book)`** — dacă acea carte este în listă, elimin-o și returnează `True`. Altfel returnează `False`. Folosește același obiect Book care a fost împrumutat.
4. **`StudentMember.__init__(name, school)`** — apelează constructorul părinte cu limita `3`, apoi salvează `school` ca atribut.
5. **`StudentMember.borrow_book(book)`** — respinge cărțile din categoria `"reference"`. Pentru celelalte, folosește metoda părinte și returnează rezultatul ei. Membrii obișnuiți pot împrumuta orice categorie.
6. **`total_pages(books)`** — folosește o buclă pentru a returna suma paginilor. Pentru o listă goală, returnează `0`.

## Exemplu
După completarea TODO-urilor, codul trebuie să producă valorile din comentarii:

```python
story = Book("The Lost Map", 120, "fiction")
science = Book("Space Journey", 80, "science")
guide = Book("Library Dictionary", 200, "reference")
student = StudentMember("Mira", "Central School")

print(student.borrow_book(story))        # True
print(student.borrow_book(science))      # True
print(student.borrow_book(guide))        # False
print(len(student.borrowed_books))       # 2
print(total_pages(student.borrowed_books))  # 200
print(student.return_book(story))        # True
print(total_pages(student.borrowed_books))  # 80
print(student.return_book(story))        # False
```

La exact trei cărți împrumutate, elevul nu poate împrumuta a patra carte. Returnarea unei cărți eliberează un loc. O operație respinsă nu modifică lista.

## Rulare și exemplu
Deschide terminalul **în folderul acestui examen** și rulează `python main.py` pentru introducere.
După completarea TODO-urilor principale, rulează exemplul scurt:

```bash
python -c "from main import run_demo; run_demo()"
```

Compară valorile afișate cu rezultatele așteptate de lângă ele. Exemplul arată utilizarea claselor; nu este o suită completă de teste. Poate produce erori sau rezultate incomplete până termini TODO-urile. Bonusul este separat.

## Sarcină opțională
Completează `count_by_category(books)`: returnează un dicționar cu numărul cărților din fiecare categorie. Pentru `[story, science, guide]` din exemplu, rezultatul este `{"fiction": 1, "science": 1, "reference": 1}`. Pentru o listă goală, returnează `{}`. Testează separat bonusul după sarcinile principale.

## Utilizare la recapitulare
Recapitulați obiectele și atributele, apoi rezolvați TODO-urile 1–3, moștenirea la 4–5 și bucla de la 6. Rulați exemplul la final.
