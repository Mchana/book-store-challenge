from lib.book import Book

def test_book_attributes():
    book = Book(1,'The Voyage Out', 'Virginia Woolf')
    assert book.id == 1
    assert book.title == 'The Voyage Out'
    assert book.author_name == 'Virginia Woolf'

def test_repr():
    book = Book(1,"Captain Underpants","Dav Plinkey")
    assert str(book) == "1 - Captain Underpants - Dav Plinkey"

def test_eq():
    book1 = Book(1, "The Stranger", "Camus")
    book2 = Book(1, "The Stranger", "Camus")

    assert book1 == book2