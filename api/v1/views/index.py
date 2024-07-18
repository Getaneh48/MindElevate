#!/usr/bin/python3
"""
Index module for book recommendations.

This module provides routes and functions to generate book recommendations based on user preferences and book genres.
"""

# Import necessary modules and classes
from models import storage
from api.v1.views import app_views
from flask import jsonify
import requests
import random
import json
from flask_jwt_extended import jwt_required, get_jwt_identity


# Route for checking the status of the API
@app_views.route('/status', methods=['GET'], strict_slashes=False)
@jwt_required()
def status():
    """
    Check the status of the API.

    This route returns a simple status message indicating that the API is operational.

    Returns:
    JSON: A status message.
    Status Code: 200 OK

    Example Response:
    {
        "status": "OK"
    }
    """
    return jsonify({"status": "OK"})

# Route for retrieving recommended books based on user preferences and genres
@app_views.route('/books_recommended', methods=['GET'], strict_slashes=False)
@jwt_required()
def books_recommended():
    """
    Retrieve recommended books based on user preferences and genres.

    This route generates book recommendations by selecting a random genre from
    the user's preferred genres and fetching books from an external API.

    Returns:
    JSON: A list of dictionaries containing recommended book information. Each dictionary includes book details.
    Status Code: 200 OK if recommendations are found.
    Status Code: 404 Not Found if no recommendations are available.

    Example Response:
    [
        {
            "id": 1,
            "title": "Recommended Book Title 1",
            "author": "Author Name 1",
            "genre": "Genre 1",
            ...
        },
        ...
    ]
    """
    auth_user = get_jwt_identity()
    user_id = auth_user['id']
    result = storage.get_books_count_by_genre(user_id)
    sorted_data = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    genres = list(sorted_data.keys())
    user = storage.get('User',user_id)
    if user.book_genere_prefs:
        prefs = json.loads(user.book_genere_prefs)
        pref_genres = storage.get_genres_by_id_list(prefs)
        print(pref_genres)
    if len(genres) <= 0:
        return jsonify({'success': False, 'message': 'No results found'}), 404
    index = random.randint(1, len(genres))
    try:
        url = f"https://www.dbooks.org/api/search/${genres[index - 1].replace(' ', '+')}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'ok':
                return jsonify(data['books'][0:10]), 200
            return jsonify({'success': False, 'message': 'Resource not found'}), 404 
        else:
            return jsonify({'success': False, 'message': 'Unable to fetch the data'}), 400
    except requests.exceptions.ConnectionError as e:
        print("Unable to communicate with the book api service")
        return jsonify({'success': False, 'message': 'Unable to communicate with the book api service'}), 503
