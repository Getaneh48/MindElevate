#!/usr/bin/python3
"""
Module: api.v1.views

This module defines the views and routes for the v1 version of the API. It includes endpoints for managing bookmarks,
books, and user interactions.
"""
from models.bookmark_book import BookmarkBook
from models import storage
from models import Book
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json
from flask_jwt_extended import jwt_required, get_jwt_identity


@app_views.route('/bookmarks', methods=['GET', 'POST', 'DELETE'],
                 strict_slashes=False)
@jwt_required()
def bookmarks():
    """
    Function: bookmarks

    This function handles the /bookmarks endpoint and provides functionality for managing bookmarks.

    Parameters:
    - request: The incoming HTTP request object.

    Returns:
    A JSON response with appropriate status code and message.
    """
    user_id = get_jwt_identity()
    if request.method == 'GET':
        """
        Get the user's bookmarked books and return them as a list.
        """
        user = storage.get('User', user_id)
        bmark_list = []
        if user.bookmarked_books:
            bookmarked = user.bookmarked_books
            for bm in bookmarked:
                bm_d = {}
                bm_d.update(bm.to_dict())
                book_dict = bm.book.to_dict()
                book_dict['genre'] = bm.book.genre.to_dict()
                bm_d.update({'book': book_dict})
                bmark_list.append(bm_d)

        return jsonify(bmark_list), 200

    if request.method == 'POST':
        """
        Add a new bookmark for a book.
        """
        if request.is_json:
            data = request.get_json()
            if 'id' not in data:
                return jsonify({'success': False, 'message': 'Bad request'}), 400
            new_bookmark = {
                    'bookmarked_by': user_id,
                    'book_id': data['id']
                    }

            try:
                # first, check if the book exists
                book = storage.get('Book', data['id'])
                if not book:
                    return jsonify({'success': False,
                                    'message': "The book doesn't exist"}), 200
                # second, check if the book is already been bookmarked
                result = storage.get_bookmarked_book_by_userid_and_bookid(user_id, data['id'])
                if result:
                    return jsonify({'success': False,
                                    'message': 'The book is already been bookmarked'}), 200
                # third, check if the book is already read, if it is,
                # there is no point bookmarking it.
                book_reading = storage.get_bookreading_by_user_and_book(user_id, data['id'])
                if book_reading:
                    return jsonify({'success': False, 
                                    'message': 'The book has already been read'}), 200

                # finally save the bookmark
                bbook = BookmarkBook(**new_bookmark)
                bbook.add()
                bbook.save()

                return jsonify({'success': True,
                                'message': 'Bookmark successfull'}), 200
            except Exception as ex:
                raise
                return jsonify({'success': False, 
                                'message': 'Unable to process the request'}), 200
        else:
            return jsonify({'success': False, 'message': 'Bad request'}), 400

    if request.method == 'DELETE':
        """
        Delete a bookmark for a book.
        """
        if request.is_json:
            data = request.get_json()
            if 'id' not in data:
                return jsonify({'success': False, 'message': 'Bad request'}), 400
            bmark = storage.get('BookmarkBook', data['id'])
            if bmark:
                bmark.delete()
                return jsonify({'success': False, 'message': 'Book removed from bookmark list'}), 200
            else:
                return jsonify({'success': False, 'message': 'Resource not found'}), 404
        else:
            return jsonify({'success': False, 'message': 'Bad request'}), 400

@app_views.route('/bookmarks/new', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_new_book_to_bookmark_list():
    """
    Function: add_new_book_to_bookmark_list

    This function handles the /bookmarks/new endpoint and allows adding a new book to the bookmark list.

    Parameters:
    - request: The incoming HTTP request object.

    Returns:
    A JSON response with appropriate status code and message.
    """
    user_id = get_jwt_identity()
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()

            try:
                # first check if the book already exists before saving
                existed_book = storage.get_book_by_title_author_and_year(data['title'],\
                        data['author'], data['pub_year'])
                if not existed_book:
                    # first try to save the new book
                    new_book = Book(**data)
                    book_id = new_book.id
                    new_book.add()
                    new_book.save()
                    
                    # store the bookmark info
                    new_bookmark = {
                        'book_id': book_id,
                        'bookmarked_by': user_id,
                        }
                    bbook = BookmarkBook(**new_bookmark)
                    bbook.add()
                    bbook.save()
                    return jsonify({'success': True, 'message': 'The book is bookmarked successfully'}), 200
                else:
                    book_id = existed_book.id
                    # check if the book is already bookmarked
                    bookmarked_book = storage.get_bookmarked_book_by_userid_and_bookid(user_id, book_id)
                    if bookmarked_book:
                        return jsonify({'success': False, 'message': 'The book is already bookmarked'}), 200
                    return jsonify({'success': True, 'message': 'The book is bookmarked successfully'}), 200

            except Exception as ex:
                # log the error

                # raise the same exception again
                raise
                return jsonify({'success': False, 'message': 'Unable to process the request'}), 200

@app_views.route('/bookmarks/<b_id>', methods=['GET', 'DELETE'], strict_slashes=False)
@jwt_required()
def bookmark(b_id):
    """
    Function: bookmark

    This function handles the /bookmarks/<b_id> endpoint and provides operations on a specific bookmark.

    Parameters:
    - b_id: The ID of the bookmark.
    - request: The incoming HTTP request object.

    Returns:
    A JSON response with appropriate status code and message.
    """
    bmark = storage.get('BookmarkBook', b_id)

    if request.method == 'GET':
        if bmark:
            bm = {}
            bm.update(bmark.to_dict())
            bm.update({'book': bmark.book.to_dict()})
            return jsonify(bm), 200
        else:
            return jsonify({'success': False, 'message': 'Resource not found'}), 404
