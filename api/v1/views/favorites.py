#!/usr/bin/python3
""" objects that handles all default RestFul API actions for books reading """
from models.book_reading import BookReading
from models.favourite_book import FavouriteBook
from models.reading_log import ReadingLog
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json

user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
@app_views.route('/favorites', methods=['GET'], strict_slashes=False)
def favorites():
    user = storage.get('User', user_id)

    favsb_list = []
    if user.favourite_books:
        favsb = user.favourite_books
        for fav in favsb:
            f = {}
            f.update(fav.to_dict())
            f.update({'book': fav.book.to_dict()})
            favsb_list.append(f)
    else:
        return jsonify({'success': False, 'message': 'Record not found'}), 404

    return jsonify(favsb_list), 200

@app_views.route('/favorites/<f_id>', methods=['GET', 'DELETE'], strict_slashes=False)
def favorite(f_id):
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
