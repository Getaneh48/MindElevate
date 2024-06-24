#!/usr/bin/python3
""" objects that handles all default RestFul API actions for books reading """
from models.bookmark_book import BookmarkBook
from models import storage
from models import Book
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json

user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
@app_views.route('/bookmarks', methods=['GET', 'POST'], strict_slashes=False)
def bookmarks():
    if request.method == 'GET':
        user = storage.get('User', user_id)
        bmark_list = []
        if user.bookmarked_books:
            bookmarked = user.bookmarked_books
            for bm in bookmarked:
                bm_d = {}
                bm_d.update(bm.to_dict())
                bm_d.update({'book': bm.book.to_dict()})
                bmark_list.append(bm_d)
        else:
            return jsonify({'success': False, 'message': 'Record not found'}), 404

        return jsonify(bmark_list), 200

    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_bookmark = {
                    'bookmarked_by': user_id,
                    'book_id': data['id']
                    }

            try:
                # first, check if the book exists
                book = storage.get('Book',data['id'])
                if not book:
                    return jsonify({'success': False, 'message': "The book doesn't exist"}), 200
                # second, check if the book is already been bookmarked
                result = storage.get_bookmarked_book_by_userid_and_bookid(user_id, data['id'])
                if result:
                    return jsonify({'success': False, 'message': 'The book is already been bookmarked'}), 200
                # third, check if the book is already read, if it is, there is no
                # point bookmarking it.
                book_reading = storage.get_bookreading_by_user_and_book(user_id, data['id'])
                if book_reading:
                    return jsonify({'success': False, 'message': 'The book has already been read'}), 200

                # finally save the bookmark
                bbook = BookmarkBook(**new_bookmark)
                bbook.add()
                bbook.save()

                return jsonify({'success': True, 'message': 'Bookmark successfull'}), 200
            except Exception as ex:
                print(ex)
                raise
                return jsonify({'success': False, 'message': 'Unable to process the request'}), 200
        else:
            return jsonify({'success': False, 'message': 'Bad request'}), 400

@app_views.route('/bookmarks/new', methods=['POST'], strict_slashes=False)
def add_new_book_to_bookmark_list():
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
def bookmark(b_id):
    bmark = storage.get('BookmarkBook', b_id)

    if request.method == 'GET':
        if bmark:
            bm = {}
            bm.update(bmark.to_dict())
            bm.update({'book': bmark.book.to_dict()})
            return jsonify(bm), 200
        else:
            return jsonify({'success': False, 'message': 'Resource not found'}), 404

    if request.method == 'DELETE':
        if bmark:
            bmark.delete()
            return ''
