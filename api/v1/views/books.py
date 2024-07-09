#!/usr/bin/python3
"""
Module that handles all default RESTful API actions for books reading.
This module provides a set of routes and functions to perform CRUD
(Create, Read, Update, Delete) operations on books and their associated data.
"""

# Import necessary modules and classes
from models.book import Book
from models import BookGenre
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json

# Route for retrieving a list of all books
@app_views.route('/books', methods=['GET'], strict_slashes=False)
def books():
    """
    Retrieve a list of all books.

    This route retrieves all the books stored in the database and returns them as a list of dictionaries.

    Returns:
    JSON: A list of dictionaries containing book information. Each dictionary
    represents a book and includes its attributes.
    Status Code: 200 OK if books are found.
    Status Code: 404 Not Found if no books are found.

    Example Response:
    [
        {
            "id": 1,
            "title": "Book Title 1",
            "author": "Author Name 1",
            "genre": "Genre 1",
            ...
        },
        {
            "id": 2,
            "title": "Book Title 2",
            "author": "Author Name 2",
            "genre": "Genre 2",
            ...
        },
        ...
    ]
    """
    books = storage.all('Book')
    if books:
        books_dict = [book.to_dict() for book in books.values()]
        return jsonify(books_dict), 200
    else:
        return jsonify({'success': False, 'message': 'Record not found'}), 404

# Route for retrieving, updating, or deleting a specific book by its ID
@app_views.route('/books/<bid>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def book(bid):
    """
    Retrieve, update, or delete a specific book by its ID.

    This route allows you to perform the following actions on a specific book
    identified by its unique ID:
     - GET: Retrieve the book's details.
     - PUT: Update the book's details.
     - DELETE: Delete the book.

    Args:
    bid (int): The unique ID of the book.

    Returns:
    JSON: The book's details as a dictionary for GET requests.
    Status Code: 200 OK for successful GET or PUT requests.
    JSON: A response message for PUT and DELETE requests.
    Status Code: 200 OK for successful PUT or DELETE requests.
    Status Code: 400 Bad Request for invalid PUT request data.
    Status Code: 404 Not Found if the book with the given ID is not found.

    Example Response for GET:
    {
        "id": 1,
        "title": "Book Title",
        "author": "Author Name",
        "genre": "Genre",
        ...
    }
    """
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

# Route for searching books based on title, author, or genre
@app_views.route('/books/search', methods=['GET'], strict_slashes=False)
def search_books():
    """
    Search for books based on title, author, or genre.

    This route allows you to search for books by providing query parameters in the request URL.

    Query Parameters:
    title (str): The title of the book to search for.
    author (str): The author of the book to search for.
    genere (str): The genre of the book to search for.

    Returns:
    JSON: A list of dictionaries containing book information that matches the search criteria.
    Status Code: 200 OK if books are found.
    Status Code: 404 Not Found if no books match the search criteria.

    Example Response:
    [
        {
            "id": 1,
            "title": "Book Title 1",
            "author": "Author Name 1",
            "genre": "Genre 1",
            ...
        },
        ...
    ]
    """
    query = request.args
    query_dict = {'title': query.get('title', None),
                  'author': query.get('author', None),
                  'genere': query.get('genere', None)}

    result = storage.search_books(query)
    result_dict = [book.to_dict() for book in result]
    return jsonify(result_dict), 200

# Route for retrieving a list of all book genres
@app_views.route('/books/genres', methods=['GET'], strict_slashes=False)
def genre_list():
    """
    Retrieve a list of all book genres.

    This route retrieves all the book genres stored in the database and returns them as a list of dictionaries.

    Returns:
    JSON: A list of dictionaries containing genre information. Each dictionary
    represents a genre and includes its attributes.
    
    Status Code: 200 OK if genres are found.

    Example Response:
    [
        {
            "id": 1,
            "name": "Genre 1",
            ...
        },
        {
            "id": 2,
            "name": "Genre 2",
            ...
        },
        ...
    ]
    """
    result = storage.all('BookGenre')
    result_dict = [genre.to_dict() for genre in result.values()]
    return jsonify(result_dict), 200

# Route for retrieving a book by its title
@app_views.route('/books/title/<title>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def get_book_by_title(title):
    """
    Retrieve, update, or delete a book by its title.

    This route allows you to perform the following actions on a book identified by its title:
     - GET: Retrieve the book's details.
     - PUT: Update the book's details.
     - DELETE: Delete the book.

    Args:
    title (str): The title of the book.

    Returns:
    JSON: The book's details as a dictionary for GET requests.
    Status Code: 200 OK for successful GET or PUT requests.
    JSON: A response message for PUT and DELETE requests.
    Status Code: 200 OK for successful PUT or DELETE requests.
    Status Code: 404 Not Found if the book with the given title is not found.

    Example Response for GET:
    {
        "id": 1,
        "title": "Book Title",
        "author": "Author Name",
        "genre": {"id": 1, "name": "Genre Name"},
        ...
    }
    """
    book = storage.get_book_by_title(title)

    if book is not None:
        book_dict = book.to_dict()
        book_dict['genre'] = book.genre.to_dict()
        return jsonify(book_dict), 200
    else:
        return jsonify({'success': False, 'message': 'book information not found'}), 404
