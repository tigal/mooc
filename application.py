# -*- coding: utf-8 -*-


from flask import Flask
from pydoc import locate


class ConstructApp(object):

    def __init__(self):
        self.extensions = {}
        self.web_app = self.init_web_app()

    def __call__(self, settings, force_init_web_app=False):
        if force_init_web_app is True:
            self.web_app = self.init_web_app()
        self.set_settings(settings)

    @staticmethod
    def init_web_app():
        return Flask(__name__, static_url_path='/static',
                     static_folder='static')  # Создаем экземпляр класса Flask-приложения

    def set_settings(self, settings):

        self.web_app.url_map.strict_slashes = settings.TRAILING_SLASH  # Указываем игнорирововать слеша в конце url
        self.web_app.config.from_object(settings)  # Передаём остальные настройки в приложение

    def init_extensions(self):
        extensions = self.web_app.config['APP_EXTENSIONS']

        if not isinstance(extensions, tuple):
            raise TypeError('The extensions must be a tuple')

        for path in extensions:
            ex = locate(path)(self)

            if ex.extension is NotImplemented:
                raise NotImplementedError('The extension is not implemented')

            else:
                if hasattr(self.web_app, ex.name):
                    raise AttributeError(f'The base application already has extension "{ex.name}"')
                setattr(self, ex.name, ex.extension)
                self.extensions[ex.name] = ex
                ex.configurate_extension()


APP = ConstructApp()
