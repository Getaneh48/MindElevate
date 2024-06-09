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
@app_views.route('/booksreading', methods=['GET'], strict_slashes=False)
def books_reading():
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
    user = storage.get('User', user_id)
    breading = []
    if user.booksreading:
        reading = user.booksreading
        for br in reading:
            breading.append(br.to_dict())

    return jsonify(breading)

@app_views.route('/books_reading/onprogress', methods=['GET'], strict_slashes=False)
def reading_onprogress():
    user = storage.get('User', user_id)
    onprogress = storage.readingOnProgress(user)
    results = []
    for item in onprogress:
        # get the all the reading log of the current reading book and convert it to dictionary
        # values
        rlog_dict = []
        if item.reading_logs:
            for rlog in item.reading_logs:
                if rlog:
                    rlog_dict.append({rlog.id: rlog.to_dict()})
        
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
        results.append(new_item)
    return jsonify(results)

@app_views.route('/books_reading/<rb_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def get_reading_book(rb_id):
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
            return jsonify({"success": True}), 200
        else:
            return abort(404)
    else:
        abort(405)
    return ''

@app_views.route('/books_reading/<br_id>/logs', methods=['GET', 'POST'], strict_slashes=False)
def reading_logs(br_id):
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
            return abort(404)

    if request.method == 'POST':
        data = request.get_json()
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
            print(remaining_pages)
            if int(data['pages_read']) > remaining_pages:
                msg = "pages read shouldn't be greater than the total pages remaining"
                return jsonify({"success":False,
                    "message": msg}), 400

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

            if total_pages_read == book.pages:
                book_reading.status = 'completed'
                # assign badge

                # save
                book_reading.save()

            # new_log.add()
            # new_log.save()
        else:
            return abort(404)

    return jsonify({"success": True}), 200

@app_views.route('books_reading/<br_id>/logs/<l_id>',
                 methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def reading_log(br_id, l_id):
    book_reading = storage.get('BookReading', br_id)

    if request.method == 'GET':
        if book_reading:
            rlogs = book_reading.reading_logs
            for rl in rlogs:
                if rl.id == l_id:
                    return jsonify(rl.to_dict()), 200

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

@app_views.route('/booksread', methods=['GET'], strict_slashes=False)
def books_read():
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
    user = storage.get('User', user_id)
    bread = []
    if user.booksreading:
        reading = user.booksreading
        for br in reading:
            if br.status == 'completed':
                book = br.book
                br_dict = {}
                for key, val in br.to_dict().items():
                    if key != 'book':
                        br_dict[key] = val
                br_dict['book'] = book.to_dict()
                bread.append(br_dict)

        return jsonify(bread), 200
    else:
        return jsonify({'status': False, 'message': 'Resource not found'}), 404

@app_views.route('/booksread/<br_id>', methods=['GET'], strict_slashes=False)
def book_read(br_id):
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
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

@app_views.route('/booksread/<br_id>/favourite', methods=['POST'], strict_slashes=False)
def add_book_to_favourites(br_id):
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
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

@app_views.route('/booksread/search', methods=['POST'], strict_slashes=False)
def search_books_read():
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
    if request.method == 'POST':
        query = request.get_json()
        result = storage.search_books_read(user_id, query)
        print(result)
    return ''
