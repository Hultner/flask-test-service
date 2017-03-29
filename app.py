from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/trailing-route/')
def trailer():
    return 'A trailing route redirects non trailing uris'


@app.route('/absolute')
def absoluter():
    return 'An absolute route will return 404 if trailing slash is added to uri'

