# -*- coding: utf-8 -*-

from flask_peewee.rest import RestAPI, Authentication

from extensions import InitBaseExtension


class InitAPI2(InitBaseExtension):

    name = 'api2'

    def init_app(self, app):  # Инициализируем RestAPI от peewee
        self.extension = RestAPI(app.web_app)
        self.extension.default_auth = Authentication(protected_methods=[])

    def configurate_extension(self):

        from models import get_models

        for m in get_models():
            self.extension.register(m)

        self.extension.setup()
