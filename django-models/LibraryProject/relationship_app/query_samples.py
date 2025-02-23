import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    return f"No books found for author {author_name}"

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return [book.title for book in library.books.all()]
    return f"No books found in library {library_name}"

# 3. Retrieve the librarian for a library
def get_librarian_of_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library and hasattr(library, 'librarian'):
        return library.librarian.name
    return f"No librarian found for library {library_name}"

# Example usage
if __name__ == "__main__":
    print(get_books_by_author("J.K. Rowling"))
    print(get_books_in_library("Central Library"))
    print(get_librarian_of_library("Central Library"))