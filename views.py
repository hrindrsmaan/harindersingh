from flask import render_template

from __init__ import app

@app.route('/', methods = ['GET', 'POST'])
def index():

	return render_template('index.html')