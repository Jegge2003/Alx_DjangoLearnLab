from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

"""
This file defines serializers for the Author and Book models.

BookSerializer:
- Serializes the Book model fields.
- Validates the publication year to ensure it is not in the future.

AuthorSerializer:
- Serializes the Author model fields.
- Includes a nested BookSerializer to represent the author's books.
- The books field is read-only and dynamically displays all related books for an author.
"""
#BookSerializer: Serializes Book model and adds custom validation for publication_year
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    
    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future"""
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(f"Publication year cannot be in the future. Current year is {current_year}.")
        return value
    
# AuthorSerializer: Serializes Author and includes a nested BookSerializer for related books.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested representation of books written by the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']