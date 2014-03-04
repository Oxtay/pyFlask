#!/usr/bin/env python

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	"""Return the name POST value"""
	
	return request.form['name']
	
if __name__ == '__main__':
	app.run(debug=True)