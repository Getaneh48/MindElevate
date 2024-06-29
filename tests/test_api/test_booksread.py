#!/usr/bin/env python3
from models import storage
from models import Book, BookReading
import requests
import lorem
import random

user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
url = 'http://localhost:5001/api/v1/'

def test_can_get_books_read():
    response = requests.get(url + 'booksread')
    assert response.status_code == 200

def test_can_get_book_completed():
    bookr_id = add_new_book_reading('completed')
    response = requests.get(url + 'booksread/' + bookr_id)
    assert response.status_code == 200

def test_can_get_book_on_progress():
    bookr_id = add_new_book_reading()
    response = requests.get(url + 'booksread/' + bookr_id)
    print(response.json())
    assert response.status_code == 404
    assert response.json()['status'] == False
    assert response.json()['message'] == 'Resource not found'

def test_can_add_book_to_favorite():
    bookr_id = add_new_book_reading()
    bookr = storage.get('BookReading', bookr_id)
    data = {'user_id': user_id, 'bookr_id': bookr.book_id}
    response = requests.post(url + 'booksread/' + bookr_id + '/favourite')
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['message'] == 'Book added to favourites'

def add_new_book_reading(status='on progress'):
    user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
    book = {'book':{
                       'title': lorem.sentence(),
                       'author': 'Amelie G. Ramirez, Edward J. Trapido',
                       'pub_year': random.randrange(1900, 2024),
                       'pages': random.randrange(50, 2000),
                       'cover_image': '',
                       'genre_id': 'f1e94135-76e6-466d-b06a-7dbdbf39a46e',
                   },
                   'reading_info': {
                       'pages_per_day': random.randrange(1, 100),
                       'pages_per_hour': random.randrange(1, 24),
                       'days_to_finish': random.randrange(1, 365),
                   },
             }
    # first save the book
    new_book = Book(**book['book'])
    book_id = new_book.id
    storage.add(new_book)
    storage.save()

    # Reading goal data
    reading_goal_data = {
                    'user_id': user_id,
                    'book_id': book_id,
                    'pages_per_day': book['reading_info']['pages_per_day'],
                    'hours_per_day': book['reading_info']['pages_per_hour'],
                    'expected_completion_day': book['reading_info']['days_to_finish'],
                    'status': status,
                    }

    new_book_reading = BookReading(**reading_goal_data)
    bookr_id = new_book_reading.id
    new_book_reading.add()
    new_book_reading.save()

    return bookr_id
