from app import app
from flask import render_template, request, send_from_directory

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

