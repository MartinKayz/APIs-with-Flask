from flask import Flask, abort
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/about")
def about_page():
    return "<p> This is the about to page </p>"

@app.route('/capitalize/<word>/')
def capitalize(word):
    return "<h1>{}</h1>".format(escape(word.capitalize()))

@app.route("/add/<int:n1>/<int:n2>/")
def add(n1, n2):
    return "<h2>{}</h2>".format(escape(n1 + n2))

@app.route("/users/<int:user_id>/")
def greet_user(user_id):
    users = ['John', 'Mary', 'Samson']
    try:
        return "<h1> Hello {} </h1>".format(users[user_id])
    except:
        abort(404)