#!/usr/bin/env python3
from models import storage
from models import Book
from models import BookGenre
import requests
import lorem
import random

url = 'http://localhost:5001/api/v1'
def test_can_get_books():
    response = requests.get(url + '/books')
    assert response.status_code == 200
    assert isinstance(response.json(), list) == True

def test_can_get_book():
    b_id = add_new_book()
    response = requests.get(url + '/books/' + b_id)
    assert response.status_code == 200
    assert response.json()['id'] == b_id

def test_can_put_book():
     b_id = add_new_book()
     author = 'updated author'
     data = {'author': author}
     response = requests.put(url + '/books/' + b_id, json=data)
     assert response.status_code == 200
     updated_book = storage.get('Book', b_id)
     assert updated_book.author == author

def test_can_get_book_by_title():
    b_id = add_new_book()
    book = storage.get('Book', b_id)

    response = requests.put(url + '/books/title/' + book.title)
    assert response.status_code == 200
    assert response.json()['title'] == book.title

def test_can_get_non_existent_book():
    response = requests.get(url + '/books/title/' + lorem.sentence())
    assert response.status_code == 404

def add_new_book():
    genres = storage.all('BookGenre')
    genre_id = ''
    for key, val in genres.items():
        genre_id = val.id
        break

    new_book = {
            'title': lorem.sentence(),
            'author': lorem.sentence(),
            'genre_id': genre_id,
            'pub_year': random.randint(1900, 2024),
            'pages': random.randint(50, 2000)
            }

    book = Book(**new_book)
    book_id = book.id
    book.add()
    book.save()

    return book_id

