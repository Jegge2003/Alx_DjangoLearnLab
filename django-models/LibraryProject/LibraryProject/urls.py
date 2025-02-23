"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from relationship_app.views import list_books, LibraryDetailView
from django.http import HttpResponse  # Temporary home page
from django.contrib import admin
from django.urls import path
from relationship_app.views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app.views import user_login, user_logout, user_register
from relationship_app import views
from relationship_app import admin_view, librarian_view, member_view

# Temporary function-based view for the home page
def home(request):
    return HttpResponse("<h1>Welcome to the Library Project</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('register/', views.register, name='register'),  # User registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # ✅ Built-in login view with custom template
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), 
    path('admin-dashboard/', admin_view.admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view.librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_view.member_dashboard, name='member_dashboard'),

]
