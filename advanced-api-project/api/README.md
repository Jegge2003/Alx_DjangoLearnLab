# Books API - CRUD Views

## Views Overview
- **BookListView**: Returns a list of all books. Public access.
- **BookDetailView**: Returns details for a specific book. Public access.
- **BookCreateView**: Creates a new book. Requires authentication.
- **BookUpdateView**: Updates a book. Requires authentication.
- **BookDeleteView**: Deletes a book. Requires authentication.

## Endpoints
- `GET /books/`
- `GET /books/<id>/`
- `POST /books/create/`
- `PUT /books/<id>/update/`
- `DELETE /books/<id>/delete/`

## Permissions
- Public access for reading books.
- Authenticated users required for creating, updating, and deleting.

## Custom Behavior
- `perform_create()` ensures custom logic on creation.
- `perform_update()` allows hooks on update actions.

# Book API - Advanced Querying Features

## Filtering
- Filter books by title, author, or publication year.
- Example:
  - `/api/books/?title=The Alchemist`
  - `/api/books/?author=1`

## Search
- Search books by title or author name.
- Example:
  - `/api/books/?search=Python`

## Ordering
- Order books by title or publication year.
- Example:
  - `/api/books/?ordering=title`
  - `/api/books/?ordering=-publication_year`


# Testing API Views for Books

## How to Run Tests
Run the following command:



## What is Tested?
- CRUD operations for Book model
- Filtering by title, author, and publication year
- Search by title and author's name
- Ordering by title and publication year
- Permissions and authentication

## Example Endpoints Tested
- `/api/books/` (GET, POST)
- `/api/books/<pk>/` (GET)
- `/api/books/<pk>/update/` (PUT)
- `/api/books/<pk>/delete/` (DELETE)

## Authenticated vs Unauthenticated
- Unauthenticated users can only list and retrieve.
- Only authenticated users can create, update, and delete books.
