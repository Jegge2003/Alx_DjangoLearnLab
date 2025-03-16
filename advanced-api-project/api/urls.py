from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve the details of a single book by its ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update an existing book (must specify which book by its primary key)
    path('books/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book (must specify which book by its primary key)
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]
