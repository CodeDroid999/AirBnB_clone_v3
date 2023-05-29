#!/usr/bin/python3
"""Module for the application"""
from flask import Flask
from flask import jsonify
from api.v1.views import app_views
from models import storage
app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_appcontext(exception):
    """tears down the app contets"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """returns not found error"""
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":
    import os
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)