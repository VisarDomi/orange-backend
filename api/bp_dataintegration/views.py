from . import bp
from . import domain


@bp.route("/books", methods=["GET"])
def get_books():

    books = domain.get_books()
    print("books", books)
    return books
