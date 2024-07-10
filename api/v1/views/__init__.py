#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.books_reading import *
from api.v1.views.favorites import *
from api.v1.views.bookmarks import *
from api.v1.views.books import *
from api.v1.views.booksread import *
from api.v1.views.account import *
