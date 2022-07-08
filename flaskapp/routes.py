from flask import render_template, Flask, request
from flaskapp import app

@app.route('/')
@app.route('/index')
@app.route('/menu')
def index():
    return render_template('index.html', title='Home')
