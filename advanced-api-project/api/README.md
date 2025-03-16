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

