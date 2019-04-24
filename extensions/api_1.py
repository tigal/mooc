# -*- coding: utf-8 -*-

from flask_restful import Api
from extensions import InitBaseExtension


class InitAPI1(InitBaseExtension):

    name = 'api1'

    def init_app(self, app):  # Инициализируем API на flask_restful

        # from utils import add_request_arg
        self.extension = Api(app.web_app, prefix='/ws')

    def configurate_extension(self):

        from services import get_services
        for view, urls in get_services():
            self.extension.add_resource(view, urls)
