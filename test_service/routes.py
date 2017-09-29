"""URI Routes of the flask application

Author: Alexander Hultnér, 2017

Provides the standard routes to the Flask application
"""
from flask import (url_for,
                   request,
                   abort,
                   make_response,
                   redirect,
                   session)
from test_service import app
from test_service.db import note


def ensure_params(given, required):
    return given and all(param in request.json for param in required)

@app.route('/')
def index():
    """Root index of the webserver"""
    return 'Index Page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Method responsible for handling user login api"""
    error = None
    if request.method == 'POST':
        if not ensure_params(request.json, ('password', 'username')):
            abort(400)

        if _valid_login(request.json['username'],
                        request.json['password']):
            return _log_the_user_in(request.json['username'])

        error = 'Invalid username or password'
        return error, 401
    else:
        return 'Log in by POSTing'


@app.route('/restricted')
def restricted():
    """A route which requires to be logged in"""
    return redirect(url_for('login'))


def _valid_login(username, password):
    """Placeholder login method"""
    return username == 'hultner' and password


def _log_the_user_in(username):
    """Placeholder login method"""
    resp = make_response('Successfully logged in as %s' % username)
    session['username'] = username
    resp.set_cookie('user', username)
    return resp


@app.route('/user/<username>')
def profile(username):
    """Show the user profile for that user"""
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """Show the post with the given id, the id is an integer"""
    return 'Post %d' % post_id


@app.route('/hello')
def hello_world():
    """Hello World route!"""
    return 'Hello, World!'


@app.route('/trailing-route/')
def trailer():
    """Testing URI with a trailing slash"""
    return 'A trailing route redirects non trailing uris'


@app.route('/absolute')
def absoluter():
    """Testing URI with absolute path (not trailing slash"""
    return 'An absolute route will return 404 if trailing slash is added ' + \
           ' to uri'


@app.route('/note/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    pass


@app.route('/note/<int:note_id>', methods=['DELETE'])
def remove_note(note_id):
    pass


@app.route('/note/', methods=['POST'])
def add_note():
    """Add a new note"""
    if ensure_params(request.json, ('title', 'body')):
        return note.add_note(request.json['title'], request.json['body'])
    else:
        error = 'Required arguments missing'
        return error, 400


@app.route('/note')
def show_notes():
    """Return all notes"""
    return 'all notes'


@app.route('/note/<int:note_id>')
def show_note(note_id):
    """Show the note with the given id, the id is an integer"""
    return 'note %d' % note_id



