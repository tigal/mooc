# -*- coding: utf-8 -*-

# Файл с локальными конфигами проекта

from settings import *


# DB_ENGINE = 'peewee.SqliteDatabase'  # раскомментировать если необходимо работать с SQLite

DATABASE = {'engine': DB_ENGINE,
            'name': 'tigal', 'user': 'tigal',  # name (имя БД) и user необходимо указать свои
            'password': 'hci2018hSe',  # password необходимо указать свой
            'host': 'team2018.piterdata.ninja', 'port': 5432}
