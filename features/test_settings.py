# -*- coding: utf-8 -*-


from local_settings import *

DB_ENGINE = 'peewee.SqliteDatabase'
DATABASE = {'engine': DB_ENGINE, 'name': 'features/ls.sqlite'}