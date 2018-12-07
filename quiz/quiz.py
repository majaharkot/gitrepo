#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#
#  Running on http://127.0.0.1:5000/  

from flask import Flask
from flask import render_template
app = Flask(__name__)

print(__name__)

@app.route("/")
def hello():
    return "<h1>Witaj na serwerze!</h1><h2>Aplikacja quiz</h2>"
    
@app.route("/strona") #definicja zasobu
def strona():
    return render_template('strona.html')
    
@app.route("/klasa")
def klasa():
    return render_template('klasa.html')


if __name__ == '__main__':
    app.run(debug=True)
