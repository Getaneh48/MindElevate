#!/usr/bin/python3
"""
Module that handles all default RESTful API actions for books read.

This module provides routes and functions to manage and retrieve information about
books that have been read by users.
"""

# Import necessary modules and classes
from models.book_reading import BookReading
from models.favourite_book import FavouriteBook
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json
from flask_jwt_extended import jwt_required, get_jwt_identity


# Route for retrieving a list of books the user has read
@app_views.route('/booksread', methods=['GET'], strict_slashes=False)
@jwt_required()
def books_read():
    """
    Retrieve a list of books the user has read.

    This route returns a list of books that the user has completed reading, along
    with additional information.

    Args:
    user_id (str): The unique ID of the user.

    Returns:
    JSON: A list of dictionaries containing information about books the user has read.
    Each dictionary includes book details, reading status, and badges earned.
    
    Status Code: 200 OK if books are found.
    Status Code: 404 Not Found if no books have been read by the user.

    Example Response:
    [
        {
            "id": 1,
            "book": {
                "id": 1,
                "title": "Book Title 1",
                "author": "Author Name 1",
                "genre": "Genre 1",
                ...
            },
            "badge": {
                "id": 1,
                "name": "Badge Name",
                ...
            },
            "status": "completed",
            ...
        },
        ...
    ]
    """
    user_id = get_jwt_identity()
    user = storage.get('User', user_id)
    bread = []
    if user.booksreading is not None:
        reading = user.booksreading
        for br in reading:
            if br.status == 'completed':
                br_dict = br.to_dict()
                if 'badge_id' in br.to_dict().keys():
                    if br.badge is not None:
                        br_dict['badge'] = br.badge.to_dict()
                book_dict = br.book.to_dict()
                book_dict['genre'] = br.book.genre.to_dict()
                br_dict['book'] = book_dict
                bread.append(br_dict)

        return jsonify(bread), 200
    else:
        return jsonify({'status': False, 'message': 'Resource not found'}), 404

# Route for managing a specific book that the user has read
@app_views.route('/booksread/<br_id>', methods=['GET', 'PUT'], strict_slashes=False)
@jwt_required()
def book_read(br_id):
    """
    Manage a specific book that the user has read.

    This route allows you to retrieve or update information about a book that the user has completed reading.

    Args:
    br_id (int): The unique ID of the book reading activity.

    Returns:
    JSON: The book reading activity details as a dictionary for GET requests.
    Status Code: 200 OK for successful GET requests.
    JSON: A response message for PUT requests.
    Status Code: 404 Not Found if the book reading activity with the given ID is not found
    or does not belong to the user.

    Example Response for GET:
    {
        "id": 1,
        "book": {
            "id": 1,
            "title": "Book Title",
            "author": "Author Name",
            ...
        },
        "badge": {
            "id": 1,
            "name": "Badge Name",
            ...
        },
        "status": "completed",
        ...
    }
    """
    if request.method == 'GET':
        user_id = get_jwt_identity()
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

# Route for adding a book to the user's favorites list
@app_views.route('/booksread/<br_id>/favourite', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_book_to_favourites(br_id):
    """
    Add a book to the user's favorites list.

    This route allows the user to mark a book as a favorite after they have completed reading it.

    Args:
    br_id (int): The unique ID of the book reading activity.

    Returns:
    JSON: A response message for POST requests.
    Status Code: 200 OK if the book is successfully added to favorites.
    Status Code: 400 Bad Request if the request is invalid.
    Status Code: 404 Not Found if the book reading activity with the given ID is not found.

    Example Response:
    {
        "success": true,
        "message": "Book added to favourites"
    }
    """
    user_id = get_jwt_identity()
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

# Route for searching for books the user has read
@app_views.route('/booksread/search', methods=['GET', 'POST'], strict_slashes=False)
@jwt_required()
def search_books_read():
    """
    Search for books the user has read.

    This route allows you to search for books that the user has completed reading based on title or genre.

    Args:
    user_id (str): The unique ID of the user.

    Query Parameters:
    title (str): The title of the book to search for.
    genere (str): The genre of the book to search for.

    Returns:
    JSON: A list of dictionaries containing search results. Each dictionary includes book details and reading status.
    Status Code: 200 OK if search results are found.
    Status Code: 404 Not Found if no matching books are found.

    Example Response:
    [
        {
            "id": 1,
            "book": {
                "id": 1,
                "title": "Book Title 1",
                "author": "Author Name 1",
                "genre": "Genre 1",
                ...
            },
            "status": "completed",
            ...
        },
        ...
    ]
    """
    user_id = get_jwt_identity()
    if request.method == 'POST':
        query = request.get_json()
        search_result = storage.search_books_read(user_id, query)

        return jsonify(search_result), 200
    
    if request.method == 'GET':
        query = request.args;
        data = {'title': query.get('title', None), 'genere': query.get('genere', None)}
        search_result = storage.search_books_read(user_id, query)

        return jsonify(search_result), 200

# Route for retrieving books read by genre
@app_views.route('/booksread/by_genres', methods=['GET'], strict_slashes=False)
@jwt_required()
def books_by_genre():
    """
    Retrieve books read by genre.

    This route returns a list of genres and the count of books the user has read in each genre.

    Returns:
    JSON: A dictionary containing genres and the count of books read in each genre.
    Status Code: 200 OK if data is found.

    Example Response:
    {
        "Genre 1": 5,
        "Genre 2": 3,
        ...
    }
    """
    user_id = get_jwt_identity()
    result = storage.get_books_count_by_genre(user_id)
    return jsonify(result), 200

# Route for retrieving the most popular books
@app_views.route('/booksread/most_pupular', methods=['GET'], strict_slashes=False)
@jwt_required()
def most_popular_books():
    """
    Retrieve the most popular books.

    This route returns a list of the most popular books based on the number of times
    they have been read, liked, or added as favorites.

    Returns:
    JSON: A dictionary containing book IDs and their popularity score.
    Status Code: 200 OK if data is found.
    Status Code: 404 Not Found if no popular books are found.

    Example Response:
    {
        "Book ID 1": 25,
        "Book ID 2": 20,
        ...
    }
    """
    most_read_books = storage.get_most_read_books()
    most_liked_books = storage.get_most_liked_books()
    most_fav_books = storage.get_most_favorited_books()

    popular_books = most_read_books + most_liked_books + most_fav_books
    popular_books = list(set(popular_books))

    if popular_books:
        return jsonify(dict(popular_books)), 200
    return jsonify({'success': False, 'message': 'Not Found'}), 404
