"""This is a testing application

This application is mainly used for testing the current state of flask and it's
capabilities.
"""

from flask import (Flask,
        url_for,
        request,
        abort,
        make_response,
        redirect,
        session)
import config

app = Flask(__name__)
app.secret_key = config.session_secret

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not request.json or not all( param in request.json for param in ('password', 'username')):
            abort(400)

        if valid_login( request.json['username'],
                        request.json['password']):
            return log_the_user_in(request.json['username'])
        else:
            error = 'Invalid username or password'
            return error, 401
    else:
        return 'Log in by POSTing'

@app.route('/restricted')
def restricted():
    return redirect(url_for('login'))


def valid_login(username, password):
    # Placeholder login method
    return username == 'hultner'

def log_the_user_in(username):
    # Placeholder login method
    resp = make_response('Successfully logged in as %s' % username)
    session['username'] = username
    resp.set_cookie('user', username)
    return resp

@app.route('/user/<username>')
def profile(username):
   # show the user profile for that user
   return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/trailing-route/')
def trailer():
    return 'A trailing route redirects non trailing uris'


@app.route('/absolute')
def absoluter():
    return 'An absolute route will return 404 if trailing slash is added to uri'

with app.test_request_context():
    print( url_for('index') )
    print( url_for('login') )
    print( url_for('login', next='/') )
    print( url_for('profile', username='John Doe') )

