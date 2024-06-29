#!/usr/bin/env python3
from models import storage
import requests

user_id = '4a2fa583-5080-49c8-9061-ef217bc42778'
url = 'http://localhost:5001/api/v1/'

def test_can_get_books_read():
    response = requests.get(url + 'booksread')
    assert response.status_code == 200
