from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

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