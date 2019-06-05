import os
import json


def get_books():
    basedir = os.path.abspath(os.path.dirname(__file__))
    basebasedir = os.path.dirname(os.path.dirname(basedir))
    static = os.path.join(basebasedir, 'static')
    new = os.path.join(static, 'book_data_json.js')

    books = []

    with open(new, encoding="utf-8") as f:
        read = f.read()
        books = json.loads(read)

    return books
