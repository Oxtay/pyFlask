#!/usr/bin/env python

from flask import Flask
from flask import redirect, render_template

app = Flask(__name__)

@app.route('/a-redirect')
def a_redirect():
	"""Redirect the user"""
	
	return redirect('http://liquorice.blogspot.com/')
    
@app.route('/a-template')
def a_template():
    """Render a page using a Jinga2 templage"""
    
    return render_templage('template.html')

@app.route('/')
def index():
	"""Homepage"""
	
	return "Hello World"
	
if __name__ == '__main__':
	app.run(debug=True)