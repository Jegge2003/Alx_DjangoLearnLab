from django.db import models

# Create your models here.

"""
This file defines the data models for the API.

Author:
- Represents a book author.
- Has a one-to-many relationship with the Book model.

Book:
- Represents a book.
- Linked to an Author using a foreign key.
"""

#Author model to store the details of the author
class Author(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#Book model:stores books and links each book to an Author
class Book(models.Model):

    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title