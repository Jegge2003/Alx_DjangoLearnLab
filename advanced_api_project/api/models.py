from django.db import models

# Create your models here.

#Author model to store the details of the author
class Author(models.Model):
    """
This file defines the data models for the API.

Author:
- Represents a book author.
- Has a one-to-many relationship with the Book model.

Book:
- Represents a book.
- Linked to an Author using a foreign key.
"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#Book model:stores books and links each book to an Author
class Book(models.Model):
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

    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title