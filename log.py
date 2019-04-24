# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from settings import LOG_PATH, DEBUG
from flask.logging import default_handler


formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')


def add_loggers(app):

    log = app.web_app.logger
    app.web_app.logger.removeHandler(default_handler)

    if DEBUG:
        level = logging.DEBUG
        log.setLevel(level)
    else:
        level = log.getEffectiveLevel()

    file_handler = RotatingFileHandler(LOG_PATH, maxBytes=10000, backupCount=1)
    file_handler.name = 'file.log'
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.name = 'console.log'
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    log.addHandler(file_handler)
    log.addHandler(console_handler)
