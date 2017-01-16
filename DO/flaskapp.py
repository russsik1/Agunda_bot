# -*- coding: utf-8 -
from flask import Flask
from db import SQLighter


app = Flask(__name__)


#перевод листа в строку для передачи по сети
def list_to_string(x):
    s = ''
    for i in x:
        s = s + i +'_'
    return s[:-1]

@app.route('/db/<request>')
def index(request):
    response = SQLighter('main.db').select(request)
    return list_to_string(response)


@app.route('/')
def home():
    return "<h1>Da bon horz</h1>"