#!/usr/bin/env python3

from api.v1.views import app_views
from models import User
from models import storage
from flask import jsonify, request
from passlib.hash import bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
import re


def check_password_complexity(password):
    """
    Checks for basic password complexity requirements.
    complexity: one or more small or capital letter, one or more digit,
                one or more punchiation character, password length should be 8 or more
    """
    lowercase = re.search(r"[a-z]", password)
    uppercase = re.search(r"[A-Z]", password)
    number = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*()_+-={}\[\]|\\:;'<,>.?/~`]", password)

    # Minimum length and character type requirements
    min_length = 8
    min_types = 3
    return (
        len(password) >= min_length and
        lowercase and uppercase and number and special and
        len([lowercase.group(), uppercase.group(), number.group(), special.group()]) >= min_types
    )

def validate_login_data(data):
    if 'username' not in data:
        return False
    if 'password' not in data:
        return False
    return True

def validate_reg_data(data):
    errors = []
    if 'username' not in data:
        errors.append("username required")
    else:
        if not re.match(r"^[a-zA-Z]+[_0-9]*[a-zA-Z]*$", data['username']):
            errors.append("Invalid username")
    if 'password' not in data:
        errors.append("password required")
    else:
        if not check_password_complexity(data['password']):
            errors.append("password does not meet complexity criteria")
    if 'email' not in data:
        errors.append("email required")
    else:
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", data['email']):
            errors.append("invalid email")

    return errors

@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    if request.method == 'POST':
        data = request.get_json()
        if validate_login_data(data):
            user = storage.get_user_by_name(data['username'])
            if user:
                try:
                    if bcrypt.verify(data['password'], user.password) is True:
                        acct_info = {
                                     'username': user.username,
                                     'first_name': user.first_name,
                                     'last_name': user.last_name,
                                     'age': user.age,
                                     'sex':user.sex,
                                     'book_genere_prefs': user.book_genere_prefs,
                                     'id': user.id
                                     }
                        access_token = create_access_token(identity=acct_info)
                        return jsonify({'success': True, 'message': 'Login successfull',\
                                        'access_token': access_token}), 200
                    else:
                        return jsonify({'success': False, 'message': 'Invalid username or password'}), 400
                except ValueError as ex:
                    print(ex)
            return jsonify({'success': False, 'message': 'Invalid username or password'}), 400
        return jsonify({'success': False, 'message': 'Bad Request'}), 400

@app_views.route('/register', methods=['POST'], strict_slashes=False)
def register():
    if request.method == 'POST':
        data = request.get_json()
        errors = validate_reg_data(data)
        if len(errors) == 0:
            user = storage.get_user_by_name(data['username'])
            # check if the username provided is taken or not
            if user is not None:
                return jsonify({'success': False, 'message': 'username already taken'}), 200

            #check if the email is already taken or not
            exist = storage.is_email_exist(data['email'])
            if exist is True:
                return jsonify({'success': False, 'message': 'email already taken'}), 200
            
            user_info = {
                    'username': data['username'],
                    'password': bcrypt.hash(data['password']),
                    'first_name': '',
                    'last_Name': '',
                    'age': data['age'] if 'age' in  data else None,
                    'sex': data['sex'] if 'sex' in data else None,
                    'email': data['email']
                    }
            try:
                new_user = User(**user_info)
                acct_info = {
                             'username': new_user.username,
                             'first_name': new_user.first_name,
                             'last_name': new_user.last_name,
                             'age': new_user.age,
                             'sex':new_user.sex,
                             'email': new_user.email,
                             'book_genere_prefs': new_user.book_genere_prefs,
                             'id': new_user.id
                             }
                new_user.add()
                new_user.save()
                access_token = create_access_token(identity=acct_info)
                return jsonify({'success': True, 'message': 'User registration is successfull',\
                                'access_token': access_token}), 200
            except Exception as ex:
                # log the exception
                print(ex)
                return jsonify({'success': False, 'message': 'Interval Server Error'}), 500
        else:
            return jsonify({'success': False, 'message': 'validation error', 'errors': errors}), 400
            
