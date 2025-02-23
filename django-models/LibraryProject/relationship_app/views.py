from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden  # ✅ Handle unauthorized access
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
import os
from django.conf import settings
from .models import UserProfile

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
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # ✅ UserCreationForm allows new users to register
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to books list after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Helper function to get template path
def get_template_path(filename):
    return os.path.join(settings.BASE_DIR, 'relationship_app', filename)

# 🟢 Check User Roles
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# 🟢 View for Admin Users
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# 🟢 View for Librarians
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# 🟢 View for Members
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# 🔹 User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # Redirect after login
    else:
        form = AuthenticationForm()
    return render(request, get_template_path('login.html'), {'form': form})

# 🔹 User Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

# 🔹 User Registration View
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, get_template_path('register.html'), {'form': form})



