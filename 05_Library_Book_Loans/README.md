# Exam 5: Library Book Loans

## Story
Reading week starts tomorrow, and the school library needs a simple way to track borrowed books. Regular members have a borrowing limit; student members have three places but cannot take reference books home.

Complete the six numbered TODOs in `main.py`. The classes, sample objects, and demo are provided. You do not need input(), external files, packages, or a menu.

## Exam Style
- Time target: 90–120 minutes.
- Focus: attributes, inheritance, `super()`, lists, conditions, and simple loops.
- Work only in `main.py`. The bonus is separate from the main tasks.
- Assume valid Book objects, positive page counts, and nonnegative borrowing limits. The same book will not be borrowed twice by the same member at the same time. No global library inventory is required.

## Main Tasks
1. **`LibraryMember.can_borrow()`** — return whether the number of borrowed books is strictly below `max_books`.
2. **`LibraryMember.borrow_book(book)`** — if there is space, append the book and return `True`. Otherwise return `False` without changing the list.
3. **`LibraryMember.return_book(book)`** — remove the book and return `True` if it is in the list; otherwise return `False`. Use the same Book object that was borrowed.
4. **`StudentMember.__init__(name, school)`** — call the parent constructor with a limit of `3`, then store `school`.
5. **`StudentMember.borrow_book(book)`** — reject category `"reference"`; otherwise use and return the parent method's result. Regular members may borrow any category.
6. **`total_pages(books)`** — return the sum of page counts using a loop. An empty list returns `0`.

## Example
After completing the TODOs, this code should produce the values in the comments:

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

At exactly three borrowed books, a student must be refused a fourth. Returning a book frees one place. A rejected operation must leave the list unchanged.

## Run and Try the Example
Open a terminal **inside this exam's folder** and run `python main.py` for the introduction.
After completing the main TODOs, run the small demo:

```bash
python -c "from main import run_demo; run_demo()"
```

Compare the printed values with the expected values alongside them. The demo is a short usage example, not a complete test suite. It may fail or show unfinished results until you complete the TODOs. The optional task is separate.

## Optional Task
Complete `count_by_category(books)`. Return a dictionary counting books in each category. For `[story, science, guide]` from the example, return `{"fiction": 1, "science": 1, "reference": 1}`. An empty list returns `{}`. Test this separately after finishing the main tasks.

## Suggested Session Flow
Use this exam for guided recap: review objects and attributes, then tackle TODOs 1–3, inheritance in TODOs 4–5, and the loop in TODO 6. Run the demo at the end.
