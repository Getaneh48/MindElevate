#!/usr/bin/env python3

from models import storage
import requests
import lorem
import random

url = 'http://localhost:5001/api/v1/register'
url_login = 'http://localhost:5001/api/v1/login'

def test_account_login():
    data = {'username':'Dolorem', 'password': 'e$l@50Th'}
    resp = requests.post(url_login, json=data)
    assert resp.status_code == 200
    assert resp.json()['success'] == True
    assert 'access_token' in resp.json().keys() 

def test_account_login_invalid_username():
    data = {'username':'Dolorem8', 'password': 'e$l@50Th'}
    resp = requests.post(url_login, json=data)
    assert resp.status_code == 400

def test_account_registration():
    username = random.choice(lorem.sentence().split())
    first_name = random.choice(lorem.sentence().split())
    lname = random.choice(lorem.sentence().split())
    data = {'username':username, 'password': 'e$l@50Th', 'first_name': first_name, 'last_name': lname}
    resp = requests.post(url, json=data)
    print(resp)
    assert resp.status_code == 200
    assert resp.json()['success'] == True

def test_account_registration_username_exists():
    data = {'username':'getaneh', 'password': 'e$l@50Th', 'first_name': 'get', 'last_name': 'al'}
    resp = requests.post(url, json=data)
    print(resp.json())
    assert resp.status_code == 200
    assert resp.json()['success'] == False
    assert resp.json()['message'] == 'username already taken'

def test_account_registration_password_complexity_fail():
    username = lorem.sentence().split()[0]
    data = {'username':username, 'password': '1234567', 'first_name': 'get', 'last_name': 'al'}
    resp = requests.post(url, json=data)
    assert resp.status_code == 400
    assert resp.json()['success'] == False
    assert resp.json()['message'] == 'validation error'

def test_account_registration_for_missing_required_attributes():
    username = lorem.sentence().split()[0]
    data = {'username':username, 'password': 'e$l@50Th', 'first_name': 'get'}
    resp = requests.post(url, json=data)
    assert resp.status_code == 400
    assert resp.json()['success'] == False

def test_account_registration_for_empty_username():
    data = {'username':'', 'password': 'e$l@50TH', 'first_name': 'get', 'last_name': 'ggg'}
    resp = requests.post(url, json=data)
    print(resp.json())
    assert resp.status_code == 400
    assert resp.json()['success'] == False
