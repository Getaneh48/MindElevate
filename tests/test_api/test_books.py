#!/usr/bin/env python3
from models import storage
import requests

url = 'http://localhost:5001/api/v1'
def test_can_get_books():
    response = requests.get(url + '/books')
    assert response.status_code == 200
    assert isinstance(response.json(), list) == True
