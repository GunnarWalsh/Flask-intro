from flask_app import app
from flask import render_template

@app.route('/')
def welcome():
    return 'Hello World!'

@app.route('/dojo')
def ninja():
    return 'Dojo'

@app.route('/say/<string:sneaky>')
def personal(sneaky):
    return f'Hi {sneaky}'

@app.route('/repeat/<int:num>/<string:subject>')
def repeat(subject , num):
    return f'Hi {subject * num}'