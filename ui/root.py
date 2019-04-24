# -*- coding: utf-8 -*-

from flask import render_template
from application import APP


@APP.web_app.route('/')
def hello():
    return render_template('root/main.html', title='Главная', content='Hello World!')