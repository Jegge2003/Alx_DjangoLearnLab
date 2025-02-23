from django.shortcuts import render
from django.views.generic.detail import DetailView  # Correct import
from .models import Book, Library

# Function-Based View (FBV) - Lists all books
def list_books(request):
    """Function-based view to list all books with their authors"""
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})  # ✅ No "relationship_app/" prefix

# Class-Based View (CBV) - Displays details for a specific library
class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library"""
    model = Library
    template_name = 'library_detail.html'  # ✅ No "relationship_app/" prefix
    context_object_name = 'library'
