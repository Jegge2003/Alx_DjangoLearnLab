import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Using `.get()` instead of `.filter().first()`
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"No books found for author {author_name}"

# 2. List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Using `.get()` to ensure only one result
        return [book.title for book in library.books.all()]
    except Library.DoesNotExist:
        return f"No books found in library {library_name}"

# 3. Retrieve the librarian for a library
def get_librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Fetch library directly
        return library.librarian.name if hasattr(library, 'librarian') else f"No librarian assigned for {library_name}"
    except Library.DoesNotExist:
        return f"No librarian found for library {library_name}"

# Example usage
if __name__ == "__main__":
    print(get_books_by_author("J.K. Rowling"))
    print(get_books_in_library("Central Library"))
    print(get_librarian_of_library("Central Library"))