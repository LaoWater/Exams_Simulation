# Python Exams Simulation

Three Python practice exams for classroom recap and independent exam simulations. Each exam contains a small story, guided TODOs, English and Romanian instructions, and a short demo showing actual and expected results.

[Instrucțiuni în română](README_RO.md)

## Choose an exam

| Exam | Practice focus |
| --- | --- |
| [04 — Harbor Distress Log](04_Harbor_Distress_Log/README.md) | File reading, strings, filtering, counting |
| [05 — Library Book Loans](05_Library_Book_Loans/README.md) | Inheritance, borrowing limits, returning books |
| [06 — School Trip Registration](06_School_Trip_Registration/README.md) | Inheritance, registration, age rules, totals |

For a recap followed by a simulation, work through **05 together**, then use **06 independently**. Allow 90–120 minutes for a full exam; choose fewer tasks if the recap shares the same session. Exam 04 is separate practice for files and strings.

## Getting started

Use Python 3. No third-party packages are needed.

1. Open one exam folder and read its README.
2. Run `python main.py` to see the introduction.
3. Complete the numbered TODOs in that folder's `main.py`.
4. Run the short demo from the same folder:

```bash
python -c "from main import run_demo; run_demo()"
```

The demo prints a few results alongside their expected values. It may fail or produce incomplete results before you finish the TODOs. It is a usage example, not a comprehensive test suite or an automatic grade. Try another input yourself to check your understanding.

The optional task in each exam is for extra practice after the main tasks. Starter files intentionally contain no completed solutions.

## Repository layout

Each numbered folder is a standalone exercise. Exam 04 also includes `transmission.txt`; its code locates that file beside `main.py`.

This collection continues the history of the former `Exam-04-The-Cipher-Anomaly` repository.

Student submissions belong inside the corresponding exam: `<exam>/Students/<student>/`. For example, [Liviu’s submission for exam 04](04_Harbor_Distress_Log/Students/Liviu/main.py). Keep each submission’s supporting files beside its code.
