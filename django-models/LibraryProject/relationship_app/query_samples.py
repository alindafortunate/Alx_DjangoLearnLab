from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
Book.objects.filter(author__id=1)

# List all books in a library.
library_name = Library.objects.create(name="Science")
library1 = Library.objects.get(name=library_name)
library1.books.all()

# Retrieve the librarian for a library.
Librarian.objects.get(library__id=1)
