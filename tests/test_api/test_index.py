#!/usr/bin/env python3

import requests

def test_server_status():
    url = 'http://localhost:5001/api/v1/status'
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json()['status'] == 'OK'

def test_can_get_recommended_books():
    url = 'http://localhost:5001/api/v1/books_recommended'
    response = requests.get(url)
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list) == True
    assert len(data) > 0
