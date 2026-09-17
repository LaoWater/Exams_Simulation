# Simulări de examen Python

Trei exerciții pentru recapitulare la clasă și simulări individuale. Fiecare examen include o poveste scurtă, TODO-uri ghidate, instrucțiuni în română și engleză și un exemplu care afișează rezultatele obținute lângă cele așteptate.

[English instructions](README.md)

## Alege un examen

| Examen | Concepte exersate |
| --- | --- |
| [04 — Jurnalul de urgență al portului](04_Harbor_Distress_Log/README_RO.md) | Citirea fișierelor, șiruri, filtrare, numărare |
| [05 — Împrumuturi la bibliotecă](05_Library_Book_Loans/README_RO.md) | Moștenire, limite de împrumut, returnarea cărților |
| [06 — Înscrieri pentru excursie](06_School_Trip_Registration/README_RO.md) | Moștenire, înscriere, vârstă minimă, totaluri |

Pentru recapitulare urmată de simulare, rezolvați **05 împreună**, apoi **06 individual**. Alocați 90–120 de minute pentru un examen complet; alegeți mai puține sarcini dacă includeți și recapitularea în aceeași sesiune. Examenul 04 este un exercițiu separat pentru fișiere și șiruri de caractere.

## Cum lucrezi

Ai nevoie de Python 3, fără pachete externe.

1. Deschide folderul unui examen și citește instrucțiunile.
2. Rulează `python main.py` pentru introducere.
3. Completează TODO-urile numerotate din acel `main.py`.
4. Rulează exemplul scurt din același folder:

```bash
python -c "from main import run_demo; run_demo()"
```

Exemplul afișează câteva rezultate lângă valorile așteptate. Poate produce erori sau rezultate incomplete până termini TODO-urile. Este un exemplu de utilizare, nu o suită completă de teste și nici o notare automată. Încearcă și alte date pentru a verifica dacă ai înțeles.

Sarcina opțională este pentru practică suplimentară după sarcinile principale. Fișierele de start nu conțin soluțiile completate.

## Structură

Fiecare folder numerotat este un exercițiu independent. Examenul 04 include și `transmission.txt`, pe care codul îl caută lângă `main.py`.

Această colecție continuă istoricul fostului repository `Exam-04-The-Cipher-Anomaly`.

Rezolvările studenților se păstrează în examenul corespunzător: `<examen>/Students/<student>/`. De exemplu, [rezolvarea lui Liviu pentru examenul 04](04_Harbor_Distress_Log/Students/Liviu/main.py). Fișierele auxiliare rămân lângă codul rezolvării.
