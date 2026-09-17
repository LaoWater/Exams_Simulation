# Examen 6: Înscrieri pentru excursia școlară

## Povestea
Școala pregătește o excursie. Profesorii trebuie să înscrie participanții, să respecte numărul de locuri și să calculeze suma încasată din bilete. O excursie cu ghid are și o regulă de vârstă minimă.

Completează cele șase TODO-uri numerotate din `main.py`. Structura, participanții pentru exemple și un exemplu de rulare sunt oferite. Nu ai nevoie de input(), fișiere externe, pachete sau meniu.

## Format
- Timp orientativ: 90–120 de minute.
- Concepte: atribute, moștenire, `super()`, adăugare în liste, condiții și bucle simple.
- Lucrează doar în `main.py`. Bonusul este independent de sarcinile principale.
- Presupune că primești obiecte Participant valide, capacități și vârste întregi nenegative și prețuri nenegative. Fiecare participant este înscris cel mult o dată la aceeași excursie; nu trebuie să detectezi duplicate.
- În acest exercițiu, un **elev** este un participant cu vârsta **sub 18 ani**. Prețurile biletelor sunt deja date: nu calculezi reduceri sau taxe.

## Sarcini principale
1. **`Trip.available_seats()`** — returnează capacitatea minus numărul participanților înscriși.
2. **`Trip.register(participant)`** — dacă există un loc liber, adaugă participantul și returnează `True`. Altfel returnează `False`, fără să modifici lista.
3. **`Trip.total_income()`** — folosește o buclă pentru a aduna `ticket_price` pentru participanții acceptați. O excursie fără participanți returnează `0`.
4. **`GuidedTrip.__init__(destination, capacity, min_age)`** — apelează constructorul părinte, apoi salvează `min_age` ca atribut.
5. **`GuidedTrip.register(participant)`** — respinge participanții cu vârsta sub `min_age`. Pentru ceilalți, folosește metoda părinte de înscriere și returnează rezultatul ei. Vârsta egală cu minimul este acceptată. O excursie obișnuită, Trip, nu are restricție de vârstă.
6. **`count_students(participants)`** — folosește o buclă pentru a număra participanții cu vârsta sub `18` ani. O listă goală returnează `0`.

## Exemplu
După completarea TODO-urilor:

```python
ana = Participant("Ana", 12, 30)
elena = Participant("Elena", 18, 50)
luca = Participant("Luca", 10, 20)
radu = Participant("Radu", 16, 30)
trip = GuidedTrip("Mountain Observatory", capacity=2, min_age=12)

print(trip.register(luca))       # False: prea mic
print(trip.available_seats())    # 2: respingerea nu ocupa un loc
print(trip.register(ana))        # True: exact varsta minima
print(trip.register(elena))      # True
print(trip.register(radu))       # False: nu mai sunt locuri
print(trip.available_seats())    # 0
print(trip.total_income())       # 80
print(count_students(trip.participants))  # 1
```

Doar Ana și Elena sunt înscrise. Biletele lor contribuie cu `30 + 50 = 80`. Elena are exact 18 ani, deci nu este numărată ca elev conform regulii acestui exercițiu.

## Rulare și exemplu
Deschide terminalul **în folderul acestui examen** și rulează `python main.py` pentru introducere.
După completarea TODO-urilor principale, rulează exemplul scurt:

```bash
python -c "from main import run_demo; run_demo()"
```

Compară valorile afișate cu rezultatele așteptate de lângă ele. Exemplul arată utilizarea claselor; nu este o suită completă de teste. Poate produce erori sau rezultate incomplete până termini TODO-urile. Bonusul este separat.

## Sarcină opțională
Completează `count_by_ticket_price(participants)`. Returnează un dicționar cu numărul participanților pentru fiecare preț de bilet, folosind numere drept chei. Pentru `[ana, elena, radu]`, rezultatul este `{30: 2, 50: 1}`. Pentru o listă goală, returnează `{}`. Testează separat bonusul după sarcinile principale.

## Utilizare la simulare
Folosește acest examen pentru lucru individual după recapitularea cu biblioteca. Rezolvă TODO-urile 1–3, apoi 4–6 și păstrează ultimele 10–15 minute pentru rularea exemplului. Încearcă bonusul doar după ce funcționează sarcinile principale.
