
from flask import Flask
from HelloFlask import app

@app.route('/')
def root():
    return "Axioms.io"

@app.route('/home')
def home():
    return "Hello Flask!"