#!/usr/bin/env python3

import requests
from models import storage
from models import Book
from models import BookReading
from models import ReadingLog
import lorem
import random
import json

url = 'http://localhost:5001/api/v1'
existed_book = {'book':{
                    'title': 'Fulfilling the Promise of Technology Transfer',
                    'authors': 'Koichi Hishida',
                    'year': 2020,
                    'pages': '135',
                    'image': '',
                 },
                 'reading_info': {
                        'genre': 'f1e94135-76e6-466d-b06a-7dbdbf39a46e',
                        'pages_per_day': 20,
                        'pages_per_hour': 5,
                        'days_to_finish': 10,
                 },
               }
reading_completed_book = {'book':{
                                'title': 'Fulfilling the Promise of Technology Transfer',
                                'authors': 'Koichi Hishida',
                                'year': 2020,
                                'pages': '135',
                                'image': '',
                         },
                         'reading_info': {
                                'genre': 'f1e94135-76e6-466d-b06a-7dbdbf39a46e',
                                'pages_per_day': 20,
                                'pages_per_hour': 5,
                                'days_to_finish': 10,
                         },
                         }


def test_can_list_bookreading():
    response = requests.get(url + '/booksreading')
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_can_post_bookreading():
    # check if the request made is not in proper json request 
    bad_response = requests.post(url + '/booksreading', existed_book)
    assert bad_response.status_code == 415

def test_can_post_existed_book():
    response = requests.post(url + '/booksreading', json=existed_book)
    print(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), dict) == True
    assert response.json()['success'] == False

def test_can_post_new_book():
    new_book = {'book':{
                       'title': 'Advancing the Science of Cancer in Latinos',
                       'authors': 'Amelie G. Ramirez, Edward J. Trapido',
                       'year': 2010,
                      'pages': '335',
                      'image': '',
                   },
                   'reading_info': {
                          'genre': 'f1e94135-76e6-466d-b06a-7dbdbf39a46e',
                          'pages_per_day': 20,
                          'pages_per_hour': 5,
                          'days_to_finish': 10,
                   },
                 }

    response = requests.post(url + '/booksreading', json=new_book)
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['message'] == 'The book has been saved successfully'

def test_can_list_reading_books_on_progress():
    response = requests.get(url + '/books_reading/onprogress')
    assert response.status_code == 200
    assert isinstance(response.json(), list) == True

def test_can_get_existed_book_on_progress():
    result = storage.get_book_on_reading_by_title("Advancing the Science of Cancer in Latinos")
    bid = result.id
    response = requests.get(url + '/books_reading/'+ bid)
    assert response.status_code == 200
    assert isinstance(response.json(), dict) == True
    assert response.json()['id'] == bid

def test_can_delete_existed_book_on_progress():
    result = storage.get_book_on_reading_by_title("Advancing the Science of Cancer in Latinos")
    bid = result.id
    response = requests.delete(url + '/books_reading/'+ bid)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['message'] == 'book reading information deleted successfully'

def test_can_post_reading_logs():
    br_id = add_new_book_reading()
    logs = {'br_id': br_id, 'pages_read': 10, 'hours_read': 2}
    response = requests.post(url + f"/books_reading/{br_id}/logs", json=logs)
    assert response.status_code == 200

def test_can_post_reading_logs_morethan_book_total_pages():
    br_id = add_new_book_reading()
    logs = {'br_id': br_id, 'pages_read': 4500, 'hours_read': 2}
    response = requests.post(url + f"/books_reading/{br_id}/logs", json=logs)
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['message'] == "Pages read shouldn't be greater than the total pages remaining"

def test_can_post_reading_logs_with_non_existent_book_reaidng():
    logs = {'br_id': 'sdfsd345454', 'pages_read': 10, 'hours_read': 2}
    response = requests.post(url + f"/books_reading/i84ie88-937545/logs", json=logs)
    assert response.status_code == 404
    assert response.json()['success'] == False
    assert response.json()['message'] == 'book reading information not found'

def test_can_post_reading_logs_with_book_reading_completed():
    br_id = add_new_book_reading('completed')
    logs = {'br_id': br_id, 'pages_read': 40, 'hours_read': 2}
    response = requests.post(url + f"/books_reading/{br_id}/logs", json=logs)
    assert response.status_code == 200
    assert response.json()['success'] == False
    assert response.json()['message'] == 'Book reading completed'

def test_can_get_reading_log():
     br_id = add_new_book_reading('completed')
     logs = {'br_id': br_id, 'pages_read': 40, 'hours_read': 2, 'badge_id': None}
     reading_log = ReadingLog(**logs)
     reading_log.add()
     reading_log_id = reading_log.id
     reading_log.save()

     response = requests.get(url + f"/books_reading/{br_id}/logs/{reading_log_id}")
     assert response.status_code == 200
     assert isinstance(response.json(), dict) == True
     assert response.json()['id'] == reading_log_id

def test_can_put_reading_log_for_reading_completed_book():
    br_id = add_new_book_reading('completed')
    logs = {'br_id': br_id, 'pages_read': 40, 'hours_read': 2, 'badge_id': None}
    reading_log = ReadingLog(**logs)
    reading_log.add()
    reading_log_id = reading_log.id
    reading_log.save()

    new_data = {'pages_read': 38, 'hours_read': 3, 'badge_id': None}

    response = requests.put(url + f"/books_reading/{br_id}/logs/{reading_log_id}", json=new_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['success'] == False
    assert response.json()['message'] == 'Book reading completed'

def test_can_put_reading_log_for_active_reading_book():
    br_id = add_new_book_reading()
    logs = {'br_id': br_id, 'pages_read': 40, 'hours_read': 2, 'badge_id': None}
    reading_log = ReadingLog(**logs)
    reading_log.add()
    reading_log_id = reading_log.id
    reading_log.save()

    new_data = {'pages_read': 38, 'hours_read': 3, 'badge_id': None}

    response = requests.put(url + f"/books_reading/{br_id}/logs/{reading_log_id}", json=new_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['message'] == 'Update successful'

    # get the updated log from the database and test if the updated is made
    updated_log = storage.get('ReadingLog', reading_log_id)
    assert updated_log.pages_read == new_data['pages_read']

def test_can_like_book():
    br_id = add_new_book_reading()
    data = {'br_id': br_id, 'is_liked': True}
    
    response = requests.put(url + '/booksreading/like', json=data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['message'] == 'Book updated successfully'

    update_breading = storage.get('BookReading', br_id)
    assert update_breading.is_liked == True

def test_can_like_book_with_nonexistent_bookreading():
    br_id = '23434-42343-d3432-5gdfgd'
    data = {'br_id': br_id, 'is_liked': True}

    response = requests.put(url + '/booksreading/like', json=data)
    print(response.json())
    assert response.status_code == 404
    assert response.json()['success'] == False
    assert response.json()['message'] == 'Record not found'

def test_can_like_book_with_bad_request():
    br_id = '23434-42343-d3432-5gdfgd'
    data = {'br_id': br_id, 'is_liked': True}

    response = requests.put(url + '/booksreading/like', data)
    print(response.json())
    assert response.status_code == 400
    assert response.json()['success'] == False

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
