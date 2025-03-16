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
