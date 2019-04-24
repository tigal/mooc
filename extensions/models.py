# -*- coding: utf-8 -*-

from flask_peewee.db import Database
from extensions import InitBaseExtension


class InitModels(InitBaseExtension):

    name = 'db'

    def init_app(self, app):  # Инициируем работу с БД

        self.extension = Database(app.web_app)

    def configurate_extension(self):

        with self.extension.database.connection_context():
            # self.drop_tables()
            self.create_tables()

    def create_tables(self):
        self.extension.database.create_tables(self.models)  # Создаём таблицы, если их нет в БД.

    def drop_tables(self):
        self.extension.database.drop_tables(self.models)  # Дропаем все таблицы

    @property
    def models(self):
        from models import get_models
        return get_models()
