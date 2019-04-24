# -*- coding: utf-8 -*-

from functools import wraps
from flask import request
from application import APP


def add_request_arg(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        print (request.data)
        print (request.get_json())
        print (request.values)
        return view_func(**request.args.to_dict())
    return wrapper


@APP.web_app.template_filter()
def show_dir(obj):
    return dir(obj)
