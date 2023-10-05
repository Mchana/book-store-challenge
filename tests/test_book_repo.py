from lib.book import Book
from lib.book_repo import BookRepository

def test_all_book_repo(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    result = repository.all()
    assert result == [
        Book(1,'Nineteen Eighty-Four', 'George Orwell'),
        Book(2,'Mrs Dalloway', 'Virginia Woolf'),
        Book(3,'Emma', 'Jane Austen'),
        Book(4,'Dracula', 'Bram Stoker'),
        Book(5,'The Age of Innocence', 'Edith Wharton')
    ]