#!/usr/bin/env python3
import requests
from models import storage
from models import Book, BookReading
import lorem
import random

url = 'http://localhost:5001/api/v1/'

def test_can_get_bookmarks():
    response = requests.get(url + 'bookmarks')
    assert response.status_code == 200
    assert isinstance(response.json(), list) == True

def test_can_post_non_existent_book_for_bookmark():
    data = {'id': '53453-434'}
    response = requests.post(url + 'bookmarks', json=data)
    assert response.status_code == 200
    assert response.json()['success'] == False
    assert response.json()['message'] == "The book doesn't exist"

def test_can_post_bookmarking_for_reading_completed_book():
    br_id = add_new_book_reading('completed')
    saved_r = storage.get('BookReading', br_id)
    data = {'id': saved_r.book_id}
    response = requests.post(url + 'bookmarks', json=data)
    assert response.status_code == 200
    assert response.json()['success'] == False

def test_can_post_new_bookmark():
    book_id = create_new_book()
    data = {'id': book_id}
    response = requests.post(url + 'bookmarks', json=data)
    assert response.status_code == 200
    assert response.json()['success'] == True

def test_can_post_bad_request():
    book_id = create_new_book()
    data = {'id': book_id}
    response = requests.post(url + 'bookmarks', data)
    assert response.status_code == 400

def test_can_post_invalid_attribute():
    # test for an invalid attribute
    data = {'ids': '3444jd-3423'}
    response = requests.post(url + 'bookmarks', json=data)
    assert response.status_code == 400

def create_new_book():
    book = {   
        'title': lorem.sentence(),
        'author': lorem.sentence(),
        'pub_year': random.randrange(1900, 2024),
        'pages': random.randrange(50, 2000),
        'cover_image': '',
        'genre_id': 'f1e94135-76e6-466d-b06a-7dbdbf39a46e',
    }

    new_book = Book(**book)
    book_id = new_book.id
    storage.add(new_book)
    storage.save()

    return book_id


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
