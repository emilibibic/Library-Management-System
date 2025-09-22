# library_manager.py
from __future__ import annotations
from typing import List, Optional
from book import Book


def add_book(library: List[Book]) -> None:
    """Prompt for book info, create a Book, and append it to library."""
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    isbn = input("Enter ISBN: ").strip()

    if not title or not author or not isbn:
        print("All fields (title, author, ISBN) are required.")
        return

    library.append(Book(title, author, isbn))
    print("Book added!\n")


def list_books(library: List[Book]) -> None:
    """Print all books in the library using Book.__str__."""
    if not library:
        print("No books in the library yet.\n")
        return

    print("\n--- Library Books ---")
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book}")
    print()


def find_book(library: List[Book], query: str) -> Optional[Book]:
    """Return a book whose title or author matches query (case-insensitive)."""
    q = query.strip().lower()
    for book in library:
        if book.title.lower() == q or book.author.lower() == q:
            return book
    return None


def main() -> None:
    my_library: List[Book] = []

    while True:
        print("Library Manager")
        print("1) Add a new book")
        print("2) List all books")
        print("3) Find a book (by exact title or author)")
        print("4) Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_book(my_library)
        elif choice == "2":
            list_books(my_library)
        elif choice == "3":
            query = input("Enter exact title or author: ")
            result = find_book(my_library, query)
            if result:
                print(f"Found: {result}\n")
            else:
                print("No matching book found.\n")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.\n")


if __name__ == "__main__":
    main()
