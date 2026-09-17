# Examen 4: Jurnalul de Urgență al Portului

## Povestea
În timpul unei furtuni pe coastă, un punct de coordonare portuar primește un jurnal text deteriorat de la sistemul radio al unui far. Jurnalul a fost salvat în `transmission.txt`, dar unele linii reprezintă doar interferențe (static). Sarcina ta este să cureți jurnalul și să reconstruiești mesajul final de urgență.

Acest examen menține totul simplu și lizibil. Munca principală are loc în `main.py`, iar fișierul text este singurul element de intrare suplimentar.

## Formatul Examenului
- Timp alocat: 90 - 120 minute
- Fișierul principal: `main.py`
- Fișier suplimentar: `transmission.txt`
- Focus: citirea fișierelor, curățarea șirurilor de caractere, adăugarea în liste, unirea șirurilor de caractere, bucle, numărare de bază

## Sarcini Principale
1. Completează `load_clean_lines(filepath)`:
   - deschide fișierul
   - elimină caracterele de rând nou (newline) folosind strip
   - ignoră rândurile goale
   - ignoră rândurile care încep cu `STATIC:`
2. Completează `BeaconBoard.add_line()` astfel încât să stocheze liniile curățate.
3. Completează `BeaconBoard.full_message()` astfel încât să returneze o singură propoziție alcătuită din toate liniile stocate.
4. Completează `BeaconBoard.count_help_calls()` astfel încât să contorizeze câte linii conțin cuvântul `help` (ajutor).
5. Completează `BeaconBoard.show_message()` astfel încât să printeze ordonat mesajul final.

## Ce Este Deja Oferit
- Povestea de început
- Un fișier jurnal de probă
- Codul de start într-un singur fișier
- O listă de teste printată când rulezi fișierul

## Exemplu de Date de Intrare și Ieșire Așteptată

**Intrare (conținut transmission.txt):**
```text
STATIC: zzzzzzt
send help immediately
STATIC: kkkrrhhh
we need help now

```

**Acțiune:**
```python
lines = load_clean_lines("transmission.txt")
board = BeaconBoard("Portul de Sud")
for line in lines:
    board.add_line(line)
```

**Rezultate Așteptate:**
- `load_clean_lines()` ar trebui să returneze exact `["send help immediately", "we need help now"]` (sărind peste liniile "STATIC:" și cele goale).
- `board.full_message()` ar trebui să returneze `"send help immediately we need help now"` (cu un spațiu între linii).
- `board.count_help_calls()` ar trebui să returneze `2`.

## Sarcina Opțională
La finalul fișierului `main.py`, completează `word_count(message)`.

Acesta este opțional. Îți cere să construiești un dicționar care contorizează de câte ori apare fiecare cuvânt în mesajul final.

## Rulare
```bash
python main.py
```
## Încearcă exemplul
După completarea TODO-urilor principale, rulează comanda din folderul examenului. Compară valorile afișate cu cele așteptate; acesta este un exemplu scurt, nu o suită completă de teste.

```bash
python -c "from main import run_demo; run_demo()"
```

Numără `help` ca un cuvânt separat folosind `line.lower().split()`, o singură dată pentru fiecare linie care îl conține. Textul oferit nu conține semne de punctuație.
