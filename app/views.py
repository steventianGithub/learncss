from app import app
from flask import url_for, render_template
from flask import request, redirect, flash, session

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
