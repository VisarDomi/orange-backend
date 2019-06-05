from . import bp
from . import domain


@bp.route("/books", methods=["GET"])
def get_books():

    books = domain.get_books()
    return books
