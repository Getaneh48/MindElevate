#!/usr/bin/python3
""" objects that handles all default RestFul API actions for books read """
from models.book_reading import BookReading
from models.favourite_book import FavouriteBook
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json

user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
@app_views.route('/booksread', methods=['GET'], strict_slashes=False)
def books_read():
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
    user = storage.get('User', user_id)
    bread = []
    if user.booksreading:
        reading = user.booksreading
        for br in reading:
            if br.status == 'completed':
                book = br.book
                br_dict = {}
                for key, val in br.to_dict().items():
                    if key != 'book':
                        br_dict[key] = val
                br_dict['book'] = book.to_dict()
                bread.append(br_dict)

        return jsonify(bread), 200
    else:
        return jsonify({'status': False, 'message': 'Resource not found'}), 404

@app_views.route('/booksread/<br_id>', methods=['GET'], strict_slashes=False)
def book_read(br_id):
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
    user = storage.get('User', user_id)
    bread = storage.get('BookReading', br_id) 
    if bread and bread.user_id == user_id:
        if bread.status == 'completed':
            book = bread.book
            br_dict = {}
            for key, val in bread.to_dict().items():
                if key != 'book':
                    br_dict[key] = val
            br_dict['book'] = book.to_dict()

            return jsonify(br_dict), 200
        else:
            return jsonify({'status': False, 'message': 'Resource not found'}), 404
    else:
        return jsonify({'status': False, 'message': 'Resource not found'}), 404

@app_views.route('/booksread/<br_id>/favourite', methods=['POST'], strict_slashes=False)
def add_book_to_favourites(br_id):
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
    book_read = storage.get('BookReading', br_id)
    if book_read:
        try:
            favbook = FavouriteBook(**{'book_id': book_read.book_id, 'user_id': user_id})
            favbook.add()
            favbook.save()
        except Exception as exp:
            return jsonify({'success': False, 'message': 'Invalid Request'}), 400

        return jsonify({'success': True, 'message': 'Book added to favourites'}), 200
    return jsonify({'success': False, 'message': 'Resource not found!'}), 404

@app_views.route('/booksread/search', methods=['GET', 'POST'], strict_slashes=False)
def search_books_read():
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
    if request.method == 'POST':
        query = request.get_json()
        search_result = storage.search_books_read(user_id, query)

        return jsonify(search_result), 200
    
    if request.method == 'GET':
        query = request.args;
        data = {'title': query.get('title', None), 'genere': query.get('genere', None)}
        search_result = storage.search_books_read(user_id, query)

        return jsonify(search_result), 200

