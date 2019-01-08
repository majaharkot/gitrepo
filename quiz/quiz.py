#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#
#  Running on http://127.0.0.1:5000/  

from flask import g
from modele import *
from views import *

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY="kjlsdajhksdfjkfujhnjutnudndri"
))

@app.before_request
def before_request():
    g.db = baza
    g.db.connect()
    
@app.after_request
def after_request(response):
    g.db.close()
    return response


if __name__ == '__main__':
    app.run(debug=True)
