#!/usr/bin/python3
""" Index """
from models import storage
from api.v1.views import app_views
from flask import jsonify
import requests
import random

user_id = '4a2fa583-5080-49c8-9061-ef217bc42778' 
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})

@app_views.route('/books_recommended', methods=['GET'], strict_slashes=False)
def books_recommended():
    result = storage.get_books_count_by_genre(user_id)
    sorted_data = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    genres = list(sorted_data.keys())
    index = random.randint(1, len(genres))
    url = f"https://www.dbooks.org/api/search/${genres[index - 1]}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data['books'][0:10]), 200
    else:
        return jsonify({'success': False, 'message': 'Unable to fetch the data'}), 400
