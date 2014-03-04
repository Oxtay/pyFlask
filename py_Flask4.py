#!/usr/bin/env python

#Exercises with Flask - Code taken from a presentation given in Linux Conference Australia - Jan 2014

from flask import Flask, render_template
from flask.ext.wtf import Form

from wtforms import TextField

class RegoForm(Form):
    """A simple rego form"""
    
    email = TextField('Email')

@app.route('/register', methods=('GET', 'POST'))
def get_register():
    """Handle the registration form"""
    
    form = RegoForm()
    
    if form.validate_on_submit():
        return "Success"
        
    return render_template('template.html', form=form)
	
if __name__ == '__main__':
    app.secret_key = 'This is really Secret'
	app.run(debug=True)