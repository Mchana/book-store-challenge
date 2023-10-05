from lib.database_connection import DatabaseConnection
from lib.book_repo import BookRepository


# connect to database
connection = DatabaseConnection()
connection.connect()

# seed database
connection.seed("seeds/book_store.sql")

book_repo = BookRepository(connection)
books = book_repo.all()

for book in book_repo.all():
    print (book)
