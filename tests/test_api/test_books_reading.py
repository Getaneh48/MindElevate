#!/usr/bin/env python3

import requests

url = 'http://localhost:5001/api/v1'

def test_can_list_bookreading():
    response = requests.get(url + '/booksreading')
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_can_post_bookreading():
    book_data = {'book':{
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

    # check if the request made is not in proper json request 
    bad_response = requests.post(url + '/booksreading', book_data)
    assert bad_response.status_code == 415

    # make a proper request
    response = requests.post(url + '/booksreading', json=book_data)
    assert response.status_code == 200
