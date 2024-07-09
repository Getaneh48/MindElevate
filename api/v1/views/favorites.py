#!/usr/bin/python3
"""
Module that handles all default RESTful API actions for managing favorite books.

This module provides routes and functions to manage and retrieve favorite books for a user.
"""

# Import necessary modules and classes
from models.book_reading import BookReading
from models.favourite_book import FavouriteBook
from models.reading_log import ReadingLog
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json

user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'

# Route for retrieving the user's favorite books
@app_views.route('/favorites', methods=['GET'], strict_slashes=False)
def favorites():
    """
    Retrieve the user's favorite books.

    This route returns a list of books that the user has marked as favorites.

    Returns:
    JSON: A list of dictionaries containing information about the user's favorite books.
    Each dictionary includes book details.
    
    Status Code: 200 OK if favorite books are found.
    Status Code: 404 Not Found if no favorite books are found for the user.

    Example Response:
    [
        {
            "id": 1,
            "user_id": "4a2fa583-5080-49c8-9061-ef217bc42778",
            "book_id": 1,
            "book": {
                "id": 1,
                "title": "Book Title 1",
                "author": "Author Name 1",
                "genre": "Genre 1",
                ...
            }
        },
        ...
    ]
    """
    user = storage.get('User', user_id)

    favsb_list = []
    if user.favourite_books:
        favsb = user.favourite_books
        for fav in favsb:
            f = {}
            f.update(fav.to_dict())
            book_dict = fav.book.to_dict()
            book_dict['genre'] = fav.book.genre.to_dict()
            f.update({'book': book_dict})
            favsb_list.append(f)
    else:
        return jsonify({'success': False, 'message': 'Record not found'}), 404

    return jsonify(favsb_list), 200

# Route for managing a specific favorite book by its ID
@app_views.route('/favorites/<f_id>', methods=['GET', 'DELETE'], strict_slashes=False)
def favorite(f_id):
    """
    Manage a specific favorite book by its ID.

    This route allows you to retrieve or delete information about a favorite book identified by its unique ID.

    Args:
    f_id (int): The unique ID of the favorite book.

    Returns:
    JSON: The favorite book details as a dictionary for GET requests.
    Status Code: 200 OK for successful GET requests.
    JSON: A response message for DELETE requests.
    Status Code: 404 Not Found if the favorite book with the given ID is not found.

    Example Response for GET:
    {
        "id": 1,
        "user_id": "4a2fa583-5080-49c8-9061-ef217bc42778",
        "book_id": 1,
        "book": {
            "id": 1,
            "title": "Book Title",
            "author": "Author Name",
            ...
        }
    }
    """
    favb = storage.get('FavouriteBook', f_id)

    if request.method == 'GET':
        if favb:
            fb = {}
            fb.update(favb.to_dict())
            fb.update({'book': favb.book.to_dict()})
            return jsonify(fb), 200
        else:
            return jsonify({'success': False, 'message': 'Resource not found'}), 404

    if request.method == 'DELETE':
        if favb:
            favb.delete()
            return ''

# Route for marking a book as favorite
@app_views.route('/favorites/add', methods=['PUT'], strict_slashes=False)
def mark_book_as_favorite():
    """
    Mark a book as favorite.

    This route allows the user to mark a book as a favorite.

    Args:
    br_id (int): The unique ID of the book reading activity.

    Returns:
    JSON: A response message for PUT requests.
    Status Code: 200 OK if the book is successfully marked as favorite.

    Example Response:
    {
        "success": true,
        "message": "Update successful"
    }
    """
    if request.method == 'PUT':
        if request.is_json:
            try:
                data = request.get_json();
                book_reading = storage.get('BookReading', data['br_id'])
                book_reading.is_favorite = True
                book_reading.save()
            
                # save the like detail to the favorites table
                fav = {
                    'user_id': book_reading.user_id,
                    'book_id': book_reading.book_id,
                }

                favorite = FavouriteBook(**fav)
                favorite.add()
                favorite.save()
            except Exception as ex:
                print(ex)

            return jsonify({'success': True, 'message': 'Update successfull'}), 200

# Route for removing a book from favorites
@app_views.route('/favorites/remove', methods=['PUT'], strict_slashes=False)
def remove_book_from_favorite():
    """
    Remove a book from favorites.

    This route allows the user to remove a book from their favorites list.

    Args:
    br_id (int): The unique ID of the book reading activity.

    Returns:
    JSON: A response message for PUT requests.
    Status Code: 200 OK if the book is successfully removed from favorites.

    Example Response:
    {
        "success": true,
        "message": "Update successful"
    }
    """
    if request.method == 'PUT':
        if request.is_json:
            data = request.get_json();
            print(data)
            book_reading = storage.get('BookReading', data['br_id'])
            print(book_reading)
            book_reading.is_favorite = False
            book_reading.save()

            return jsonify({'success': True, 'message': 'Update successfull'}), 200

# Route for removing a favorite book
@app_views.route('/favorites/remove', methods=['POST'], strict_slashes=False)
def remove_favorite_book():
    """
    Remove a favorite book.

    This route allows the user to remove a book from their favorites list by providing the ID of the favorite book.

    Args:
    id (int): The unique ID of the favorite book.

    Returns:
    JSON: A response message for POST requests.
    Status Code: 200 OK if the favorite book is successfully removed.
    Status Code: 400 Bad Request if the request is invalid.
    Status Code: 404 Not Found if the favorite book with the given ID is not found.

    Example Response:
    {
        "success": true,
        "message": "Book Removed from favorite"
    }
    """
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()

            fav_book = storage.get('FavouriteBook', data['id'])
            if fav_book:
                user_id = fav_book.user_id
                book_id = fav_book.book_id

                fav_book.delete()
                # check if the favorite book is available on the books reading table
                book_read = storage.get_bookreading_by_user_and_book(user_id, book_id)
                print(f"fav-book: {book_read}")
                if book_read:
                    book_read.is_favorite = False
                    # now , set is_favorite field of bookreading table to false
                    book_read.save()
            else:
                return jsonify({'success': False, 'message': 'Bad Request'}), 400
        else:
            return jsonify({'success': False, 'message': 'Bad Request'}), 400

        return jsonify({'success': True, 'message': 'Book Removed from favorite'}), 200

