#!/usr/bin/python3
"""
Module that handles all default RESTful API actions for book reading.

This module provides routes and functions to manage book reading activities,
including tracking reading progress, logging reading sessions, and managing favorite books.
"""

# Import necessary modules and classes
from models.book_reading import BookReading
from models.book import Book
from models.favourite_book import FavouriteBook
from models.reading_log import ReadingLog
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
import json
from datetime import date
from datetime import datetime

user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'

# Route for managing book reading activities
@app_views.route('/booksreading', methods=['GET', 'POST'], strict_slashes=False)
def books_reading():
    """
    Manage book reading activities.

    This route allows you to retrieve a list of books the user is currently reading or
    add a new book to their reading list.

    Args:
    user_id (str): The unique ID of the user.

    Returns:
    JSON: A list of dictionaries containing information about books the user is currently reading for GET requests.
    Status Code: 200 OK for successful GET requests.
    JSON: A response message for POST requests.
    Status Code: 200 OK for successful POST requests.
    Status Code: 415 Unsupported Media Type for invalid request data.
    Status Code: 500 Internal Server Error if an error occurs during book saving.

    Example Response for GET:
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
            "pages_per_day": 50,
            "hours_per_day": 2,
            "expected_completion_day": "2023-09-15",
            ...
        },
        ...
    ]
    """
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
    if request.method == 'GET':
        user = storage.get('User', user_id)
        breading = []
        if user.booksreading:
            reading = user.booksreading
            for br in reading:
                br_dict = br.to_dict()
                br_dict['book'] = br.book.to_dict()
                breading.append(br_dict)

        return jsonify(breading)

    if request.method == 'POST':
        data = request.get_json()
        if request.is_json:
            book_data = {
                'title': data['book']['title'],
                'author': data['book']['authors'],
                'genre_id': data['reading_info']['genre'],
                'pub_year': int(data['book']['year']),
                'pages': int(data['book']['pages']),
                'cover_image': data['book']['image']
            }

            try:
                # check if the book is already been saved
                results = storage.search_books({'title': data['book']['title']})
                found = False
                found_book = None
                book_id = None
                for result in results:
                    if result.title == data['book']['title'] and \
                        result.author == data['book']['authors'] and \
                        result.pub_year == int(data['book']['year']):
                            found = True
                            found_book = result
                            break
                if found:
                    book_id = found_book.id
                    # check if the book is being read or completed reading
                    reading = storage.get_reading_by_book(user_id, book_id)
                    if reading:
                        if reading.status == "completed":
                            return jsonify({'success': False, 'message': 'The book has already been read!'}), 200
                        else:
                            return jsonify({'success': False, 'message': 'Reading the book is on progress'}), 200
                else:
                    # first save the book
                    new_book = Book(**book_data)
                    book_id = new_book.id
                    storage.add(new_book)
                    storage.save()

                # Reading goal data
                reading_goal_data = {
                    'user_id': user_id,
                    'book_id': book_id,
                    'pages_per_day': data['reading_info']['pages_per_day'],
                    'hours_per_day': data['reading_info']['pages_per_hour'],
                    'expected_completion_day': data['reading_info']['days_to_finish'],
                    'status': 'on progress',
                    }

                new_book_reading = BookReading(**reading_goal_data)
                new_book_reading.add()
                new_book_reading.save()

                return jsonify({'success': True, 'message': 'The book has been saved successfully'}), 200
            except Exception as ex:
                return jsonify({'success': False, 'message': 'Error occured'}), 500
        else:
            return jsonify({'success': False, 'message': 'Bad request'}), 415

# Route for retrieving books that the user is currently reading
@app_views.route('/books_reading/onprogress', methods=['GET'], strict_slashes=False)
def reading_onprogress():
    """
    Retrieve books that the user is currently reading.

    This route returns a list of books that the user is currently reading, along with
    their reading progress and related information.

    Returns:
    JSON: A list of dictionaries containing book reading information. Each dictionary includes book
    details, reading progress, and reading logs.
    Status Code: 200 OK if books are found.

    Example Response:
    [
        {
            "id": 1,
            "book": {
                "id": 1,
                "title": "Book Title",
                "author": "Author Name",
                "genre": {"id": 1, "name": "Genre Name"},
                ...
            },
            "pages_per_day": 50,
            "hours_per_day": 2,
            "expected_completion_day": "2023-09-15",
            "reading_logs": [
                {
                    "id": 1,
                    "pages_read": 30,
                    "hours_read": 1.5,
                    "status": "incomplete",
                    "created_at": "2023-09-10"
                },
                ...
            ]
        },
        ...
    ]
    """
    user = storage.get('User', user_id)
    onprogress = storage.readingOnProgress(user)
    results = []
    for item in onprogress:
        # get all the reading log of the current reading book and convert it to dictionary
        # values
        rlog_dict = []
        today = date.today()
        if item.reading_logs:
            for rlog in item.reading_logs:
                if rlog:
                    # check if the reading log is today's log
                    if today == rlog.created_at.date():
                        rlog_dict.append(rlog.to_dict())
        
        new_item = {}
        for elm_key, val in item.to_dict().items():
            # we do this bacause the reading_logs in the item model is in object form and cannot be json
            # serialized. so, we override this property with the modified dictionary value above
            if elm_key != 'reading_logs': 
                new_item[elm_key] = val
        # reverse the reading logs rlog_dict values in descending order. this is to get
        # the latest data first
        rlog_dict.reverse()

        new_item['reading_logs'] = rlog_dict
        book_dict = item.book.to_dict();
        book_dict['genre'] = item.book.genre.to_dict()
        new_item['book'] = book_dict
        results.append(new_item)
    return jsonify(results)

# Route for managing a specific book reading activity by its ID
@app_views.route('/books_reading/<rb_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def get_reading_book(rb_id):
    """
    Manage a specific book reading activity by its ID.

    This route allows you to retrieve, update, or delete information about a book reading
    activity identified by its unique ID.

    Args:
    rb_id (int): The unique ID of the book reading activity.

    Returns:
        JSON: The book reading activity details as a dictionary for GET requests.
        Status Code: 200 OK for successful GET requests.
        JSON: The updated book reading activity details for PUT requests.
        Status Code: 200 OK for successful PUT requests.
        JSON: A response message for DELETE requests.
        Status Code: 200 OK for successful DELETE requests.
        Status Code: 404 Not Found if the book reading activity with the given ID is not found.
    
    Example Response for GET:
    {
        "id": 1,
        "book_id": 1,
        "pages_per_day": 50,
        "hours_per_day": 2,
        "expected_completion_day": "2023-09-15",
        "friend_visible": true,
        "status": "in progress",
        "book": {
            "id": 1,
            "title": "Book Title",
            "author": "Author Name",
            ...
        }
    }
    """

    if request.method == 'GET':
        book_reading = storage.get('BookReading', rb_id)
        if book_reading:
            book = book_reading.book
            print(book.to_dict())

        # create a new dictionary except for the related book object, since it is not serializable
        # automatically. we will serialize it manually and added to the new dictionary.
        bread_dict = {}
        for key, val in book_reading.to_dict().items():
            if key != 'book':
                bread_dict[key] = val
        
        # remove the book_id key since we have the entire book object
        del bread_dict['book_id']
        bread_dict['book'] = book.to_dict()

        return jsonify(bread_dict), 200

    elif request.method == 'PUT':
        data = request.get_json()
        book_reading = storage.get('BookReading', rb_id)
        if book_reading:
            book_reading.book_id = data.get('book_id', None)
            book_reading.pages_per_day = data.get('pages_per_day', None)
            book_reading.hours_per_day = data.get('hours_per_day', None)
            book_reading.expected_completion_day = data.get('expected_completion_day', None)
            book_reading.friend_visible = data.get('friend_visible', None)
            book_reading.status = data.get('status', None)
            book_reading.save()
        else:
            return abort(404)

        return jsonify(book_reading.to_dict()), 200

    elif request.method == 'DELETE':
        book_reading = storage.get('BookReading', rb_id)
        print(book_reading)
        if book_reading:
            print('deleting...')
            storage.delete()
            return jsonify({"success": True, 'message': 'book reading information deleted successfully'}), 200
        else:
            return jsonify({'success': False, 'message': 'book reading information not found'}), 404
    else:
        abort(405)
    return ''

# Route for managing reading logs for a specific book reading activity
@app_views.route('/books_reading/<br_id>/logs', methods=['GET', 'POST'], strict_slashes=False)
def reading_logs(br_id):
    """
    Manage reading logs for a specific book reading activity.

    This route allows you to retrieve a list of reading logs for a book reading activity or add a new reading log.

    Args:
        br_id (int): The unique ID of the book reading activity.

    Returns:
        JSON: A list of dictionaries containing reading log information for GET requests.
        Status Code: 200 OK for successful GET requests.
        JSON: A response message for POST requests.
        Status Code: 200 OK for successful POST requests.
        Status Code: 404 Not Found if the book reading activity with the given ID is not found.
        Status Code: 200 OK if the book reading is already completed.

    Example Response for GET:
    [
        {
            "id": 1,
            "br_id": 1,
            "pages_read": 30,
            "hours_read": 1.5,
            "status": "incomplete",
            "created_at": "2023-09-10"
        },
        ...
    ]
    """

    book_reading = storage.get('BookReading', br_id)
    if request.method == 'GET':
        if book_reading:
            rlogs = book_reading.reading_logs
            rlogs_dict = []
            for rl in rlogs:
                rlogs_dict.append(rl.to_dict())
            rlogs_dict.reverse()
            return jsonify(rlogs_dict), 200
        else:
            return jsonify({'success': False, 'message': 'book reading information not found'}), 404

    if request.method == 'POST':
        data = request.get_json()
        if 'br_id' not in data:
            data['br_id'] = br_id

        if book_reading:
            book = book_reading.book
            params = {'br_id': br_id,
                      'pages_read': data['pages_read'],
                      'hours_read': data['hours_read'],
                      'badge_id': None}

            #check if the reading the book is completed
            if book_reading.status == 'completed':
                return jsonify({'success': False, 
                                'message': "Book reading completed"}), 200

            # calculate the total pages read so far
            total_pages_read = 0
            for log in book_reading.reading_logs:
                total_pages_read += log.pages_read
            
            # check if the read page count is not more than the remaining pages
            remaining_pages = book.pages - total_pages_read
            if int(data['pages_read']) > remaining_pages:
                msg = "Pages read shouldn't be greater than the total pages remaining"
                return jsonify({"success":False,
                    "message": msg}), 200

            # check if the user is achieved the daily reading log and if did,
            # change the status to "complete" and assign a new daily achieve goal
            # badge

            if int(data['pages_read']) >= book_reading.pages_per_day:
                if int(data['hours_read']) >= book_reading.hours_per_day:
                    params['status'] = 'completed'
                    # assign badge
                    badge = storage.badge_by_type('daily')
                    if badge:
                        params['badge_id'] = badge.id
                else:
                    params['status'] = 'incomplete'
            else:
                params['status'] = 'incomplete'
            
            # save the new log
            new_log = ReadingLog(**params)
            new_log.add()
            new_log.save()

            # check if the entire book reading is completed and if it did
            # mark the status "completed" and assign a badge accordingly

            if (int(data['pages_read']) + total_pages_read) == book.pages:
                book_reading.status = 'completed'
                # assign badge
                # badge only will assigned if the user finishes the book befere
                # the finishing goal

                today = datetime.today()
                created_at = book_reading.created_at;

                diff = today - created_at
                # check at least if the user finish before 75 % of the finishing goal
                days_in_perc = int((diff.days / book_reading.expected_completion_day) * 100)
                if days_in_perc <= 75:
                    badge = storage.get_badge_by_type("page turner")
                    if badge:
                        book_reading.badge_id = badge.id
                # save
                book_reading.save()

            # new_log.add()
            # new_log.save()
        else:
            return jsonify({'success': False, 'message': 'book reading information not found'}), 404

    return jsonify({"success": True}), 200

# Route for managing a specific reading log by its ID
@app_views.route('books_reading/<br_id>/logs/<l_id>',
                 methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def reading_log(br_id, l_id):
    """
    Manage a specific reading log by its ID.

    This route allows you to retrieve, update, or delete information about a reading log identified by its unique ID.

    Args:
        br_id (int): The unique ID of the book reading activity.
        l_id (int): The unique ID of the reading log.

    Returns:
        JSON: The reading log details as a dictionary for GET requests.
        Status Code: 200 OK for successful GET requests.
        JSON: A response message for PUT requests.
        Status Code: 200 OK for successful PUT requests.
        Status Code: 404 Not Found if the reading log with the given ID is not found.
        Status Code: 200 OK if the book reading is already completed.

        Example Response for GET:
        {
            "id": 1,
            "br_id": 1,
            "pages_read": 30,
            "hours_read": 1.5,
            "status": "incomplete",
            "created_at": "2023-09-10"
        }
    """
    book_reading = storage.get('BookReading', br_id)

    if request.method == 'GET':
        if book_reading:
            rlogs = book_reading.reading_logs
            for rl in rlogs:
                if rl.id == l_id:
                    return jsonify(rl.to_dict()), 200
        else:
            return jsonify({"success", False}), 404

    if request.method == 'PUT':
        # check if reading the book is completed
        if book_reading.status == 'completed':
            return jsonify({'success': False,
                                'message': "Book reading completed"}), 200

        reading_log = storage.get('ReadingLog', l_id)
        if reading_log:
            book = book_reading.book
            reading_log = storage.get('ReadingLog', l_id)
            data = request.get_json()

            total_pages_read = 0
            for log in book_reading.reading_logs:
                total_pages_read += log.pages_read

            # check if the read page count is not more than the remaining pages
            remaining_pages = book.pages - total_pages_read
            if int(data['pages_read']) > remaining_pages:
                msg = "pages read shouldn't be greater than the total pages remaining"
                return jsonify({"success":False, 
                    "message": msg}), 400

            # check if the user is achieved the daily reading log and if did,
            # change the status to "complete" and assign a new daily achieve goal
            # badge

            if int(data['pages_read']) >= book_reading.pages_per_day:
                if int(data['hours_read']) >= book_reading.hours_per_day:
                    reading_log.status = 'completed'
                    # assign badge
                else:
                    reading_log.status = 'incomplete'
            else:
                reading_log.status = 'incomplete'

            # update the reading log
            reading_log.pages_read = data['pages_read']
            reading_log.hours_read = data['hours_read']
            reading_log.save()

            # check if the entire book reading is completed and if it did
            # mark the status "completed" and assign a badge accordingly

            if total_pages_read == book.pages:
                book_reading.status = 'completed'
                # assign badge

                # save
                book_reading.save()

            return jsonify({'success': True, 'message': 'Update successful'})
        else:
            return jsonify({'success': False, 'message': 'Reading Log Not Found'}), 404

# Route for liking or disliking a book
@app_views.route('/booksreading/like', methods=['PUT'], strict_slashes=False)
def like_book():
    """
    Like or dislike a book.

    This route allows you to update the "is_liked" status of a book reading activity.

    Args:
        br_id (int): The unique ID of the book reading activity.
        is_liked (bool): True if the book is liked, False otherwise.

    Returns:
        JSON: A response message for PUT requests.
        Status Code: 200 OK for successful PUT requests.
        Status Code: 404 Not Found if the book reading activity with the given ID is not found.

        Example Response:
        {
            "success": True,
            "message": "Book updated successfully"
        }
    """
    if request.method == 'PUT':
        if request.is_json:
            data = request.get_json()

            bookr = storage.get('BookReading', data['br_id'])
            if bookr:
                bookr.is_liked = data['is_liked']
                try:
                    bookr.save()
                except Exception as ex:
                    print(ex)

                return jsonify({'success': True, 'message': 'Book updated successfully'}), 200
            else:
                return jsonify({'success': False, 'message': 'Record not found'}), 404
        else:
            return jsonify({'success': False, 'message': 'Bad request'}), 400

# Route for retrieving all reading logs for a specific book reading activity
@app_views.route('books_reading/<br_id>/logs/all', methods=['GET'], strict_slashes=False)
def get_all_bookreading_log_summary(br_id):
    """
    Retrieve all reading logs for a specific book reading activity.

    This route returns a summary of all reading logs for a book reading activity, including
    the date and total pages read on each day.

    Args:
        br_id (int): The unique ID of the book reading activity.

    Returns:
        JSON: A list of dictionaries containing reading log summary information. Each dictionary
        includes the date and total pages read.
        
        Status Code: 200 OK if reading logs are found.
        Status Code: 404 Not Found if no reading logs are found for the given book reading activity.

    Example Response:
    [
        {
            "date": "2023-09-10",
            "total_pages": 30
        },
        ...
    ]
    """
    results = storage.get_all_readinglogs_summary(br_id)
    if results:
        logs = []
        for row in results:
            logs.append({'date': row[0].strftime("%Y-%m-%d"), 'total_pages': int(row[1])})
        
        return jsonify(logs), 200 
    else:    
        return jsonify({'success':False, 'message': 'No data found'}), 404
