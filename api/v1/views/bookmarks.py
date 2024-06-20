#!/usr/bin/python3
""" objects that handles all default RestFul API actions for books reading """
from models.bookmark_book import BookmarkBook
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json

user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
@app_views.route('/bookmarks', methods=['GET'], strict_slashes=False)
def bookmarks():
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
