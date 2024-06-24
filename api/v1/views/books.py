#!/usr/bin/python3
""" objects that handles all default RestFul API actions for books reading """
from models.book import Book
from models import BookGenre
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json

@app_views.route('/books', methods=['GET'], strict_slashes=False)
def books():
    books = storage.all('Book')
    if books:
        books_dict = [book.to_dict() for book in books.values()]
        return jsonify(books_dict), 200
    else:
        return jsonify({'success': False, 'message': 'Record not found'}), 404

@app_views.route('/books/<bid>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def book(bid):
    bk = storage.get('Book', bid)
    if bk:
        if request.method == 'GET':
            return jsonify(bk.to_dict())

        if request.method == 'PUT':
            if request.is_json:
                data = request.get_json()
                for dk in data.keys():
                    if dk in bk.to_dict().keys():
                        setattr(bk, dk, data[dk])
                bk.save()
                return jsonify({'success': True, 'message': 'Update successfull'}), 200
            else:
                return jsonify({'success': False, 'message': 'Bad request'}), 400

        if request.method == 'DELETE':
            pass
    else:
        return jsonify({'success': False, 'message': 'Record not found'})

@app_views.route('/books/search', methods=['GET'], strict_slashes=False)
def search_books():
    query = request.args
    query_dict = {'title': query.get('title', None),
                  'author': query.get('author', None),
                  'genere': query.get('genere', None)}

    result = storage.search_books(query)
    result_dict = [book.to_dict() for book in result]
    return jsonify(result_dict), 200

@app_views.route('/books/genres', methods=['GET'], strict_slashes=False)
def genre_list():
    result = storage.all('BookGenre')
    result_dict = [genre.to_dict() for genre in result.values()]
    return jsonify(result_dict), 200

@app_views.route('/books/title/<title>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def get_book_by_title(title):
    book = storage.get_book_by_title(title)
    book_dict = book.to_dict()
    book_dict['genre'] = book.genre.to_dict()
    return jsonify(book_dict), 200
