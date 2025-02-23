from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def list_books(request):
    """Function-based view to list all books with their authors"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirect to books list after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

# User Registration View
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # ✅ UserCreationForm allows new users to register
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to books list after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})