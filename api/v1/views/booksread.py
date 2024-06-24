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
                print(br)
                br_dict = br.to_dict()
                if 'badge_id' in br.to_dict().keys():
                    br_dict['badge'] = br.badge.to_dict()
                book_dict = br.book.to_dict()
                book_dict['genre'] = br.book.genre.to_dict()
                br_dict['book'] = book_dict
                bread.append(br_dict)

        return jsonify(bread), 200
    else:
        return jsonify({'status': False, 'message': 'Resource not found'}), 404

@app_views.route('/booksread/<br_id>', methods=['GET', 'PUT'], strict_slashes=False)
def book_read(br_id):
    if request.method == 'GET':
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

    if request.method == 'PUT':
        pass

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

@app_views.route('/booksread/by_genres', methods=['GET'], strict_slashes=False)
def books_by_genre():
    result = storage.get_books_count_by_genre(user_id)
    return jsonify(result), 200

@app_views.route('/booksread/most_pupular', methods=['GET'], strict_slashes=False)
def most_popular_books():
    most_read_books = storage.get_most_read_books()
    most_liked_books = storage.get_most_liked_books()
    most_fav_books = storage.get_most_favorited_books()

    popular_books = most_read_books + most_liked_books + most_fav_books
    popular_books = list(set(popular_books))

    print(f"favorited - {popular_books}")
    if popular_books:
        return jsonify(dict(popular_books)), 200
