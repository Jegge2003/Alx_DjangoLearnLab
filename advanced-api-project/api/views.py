from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Returns a list of all books. Accessible to any user.
    """
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only for unauthenticated users

    def get_queryset(self):
        queryset = Book.objects.all()
        author_id = self.request.query_params.get('author')
        if author_id is not None:
            queryset = queryset.filter(author=author_id)
        return queryset


class BookDetailView(generics.RetrieveAPIView):
    """
    Returns details of a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book. Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to customize how the book is created.
        """
        # You can associate the book with the user if needed:
        # serializer.save(owner=self.request.user)
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book by ID. Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook to customize how the book is updated.
        """
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book by ID. Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

