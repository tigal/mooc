# -*- coding: utf-8 -*-


class InitBaseExtension(object):

    name = NotImplemented  # название атрибу в базовом классе приложения

    def __init__(self, app=None):
        self.extension = NotImplemented

        if app is not None:
            self.base_check(app)
            self.init_app(app)

    def base_check(self, app):
        if self.name is NotImplemented:
            raise NotImplementedError('The extension "name" is not implemented')

    def init_app(self, app):
        raise NotImplementedError('Method "init_app" is not implemented')

    def configurate_extension(self):
        return
