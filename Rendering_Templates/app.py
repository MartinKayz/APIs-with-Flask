import datetime
from datetime import date
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('settings.py')

@app.route("/")
def hello_world():
    return render_template("index.html", utc_dt=datetime.datetime.utcnow())

@app.route('/about/')
def about_page():
    return render_template("about.html", today=date.today())

@app.route('/comments/')
def comments():
    comments = [
            'This is the first comment',
            'This is the second comment',
            'This is the third comment',
            'This is the fourth comment'
            ]
    return render_template("comments.html", comments=comments)



