from . import backend


def get_books():
    books = backend.get_books()

    return books
