class Book:
    def __init__(self, title, pages, category):
        self.title = title
        self.pages = pages
        self.category = category


class LibraryMember:
    def __init__(self, name, max_books=2):
        self.name = name
        self.max_books = max_books
        self.borrowed_books = []

    def can_borrow(self):
        # TODO 1: Return True when the member has fewer than max_books books.
        # Hint: use len(self.borrowed_books).
        if(len(self.borrowed_books) < self.max_books):
            return True
        return False
        

    def borrow_book(self, book):
        # TODO 2: If self.can_borrow() is False, return False without changing the list.
        # Otherwise append book to self.borrowed_books and return True.
        return False

    def return_book(self, book):
        # TODO 3: If book is in self.borrowed_books, remove it and return True.
        # Otherwise return False. Hint: use 'in' and list.remove(book).
        return False


class StudentMember(LibraryMember):
    def __init__(self, name, school):
        # TODO 4: Use super().__init__() with name and max_books=3.
        # Then store school in self.school.
        super().__init__(name, max_books=3)
        self.school = school

    def borrow_book(self, book):
        # TODO 5: Books with category == "reference" cannot be borrowed
        # by student members. Return False for those books.
        # For any other book, return the result of super().borrow_book(book).
        return False


# Aici se termina clasele

def total_pages(books):
    # TODO 6: Use a loop to sum the pages of all books. Empty list -> 0.
    return 0


def count_by_category(books):
    # OPTIONAL: Return a dictionary counting books in each category.
    # Example: {"fiction": 2, "science": 1}. Empty list -> {}.
    return 10


# Small example to run after completing the main TODOs.
def run_demo():
    story = Book("The Lost Map", 120, "fiction")
    guide = Book("Library Dictionary", 200, "reference")
    student = StudentMember("Mira", "Central School")
    print("Borrow story:", student.borrow_book(story), "| Expected: True")
    print("Borrow reference book:", student.borrow_book(guide), "| Expected: False")
    print("Total pages:", total_pages(student.borrowed_books), "| Expected: 120")
    # print("Return story:", student.return_book(story), "| Expected: True")




# Aici se termina functiile

def main():
    print("=== Library Book Loans - Main ===")

    run_demo()
    print('\nAfter completing the TODOs, run: python -c "from main import run_demo; run_demo()"')


if __name__ == "__main__":
    main()
