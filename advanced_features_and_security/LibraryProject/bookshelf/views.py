from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book
from django.db.models import Q
from .forms import BookForm  # Import the form
from .forms import ExampleForm

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return render(request, 'success.html')
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return render(request, 'success.html')
    return render(request, 'edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return render(request, 'success.html')
    return render(request, 'delete_book.html', {'book': book})


def search_books(request):
    query = request.GET.get('title', '')
    books = Book.objects.filter(Q(title__icontains=query))
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")  # Redirect to the list of books
    else:
        form = BookForm()
    
    return render(request, "bookshelf/book_form.html", {"form": form})


def example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form (e.g., save, send email, etc.)
            return render(request, "bookshelf/example_success.html", {"form": form})
    else:
        form = ExampleForm()
    
    return render(request, "bookshelf/example_form.html", {"form": form})

