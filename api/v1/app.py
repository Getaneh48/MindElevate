#!/usr/bin/python3
""" Flask API app """
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from flask_jwt_extended import create_access_token, get_jwt_identity,\
        jwt_required, JWTManager

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JWT_SECRET_KEY'] = 'THIS IS A SECRET KEY'
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# JWT SETUP
jwt = JWTManager(app)

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'MindElevate Restful API',
    'uiversion': 1
}

Swagger(app)


if __name__ == "__main__":
    """ Initialize and start the api server """
    host = environ.get('MELV_API_HOST')
    port = environ.get('MELV_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
