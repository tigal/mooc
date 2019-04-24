# -*- coding: utf-8 -*-

from flask_peewee.auth import Auth

from extensions import InitBaseExtension


class InitAuth(InitBaseExtension):

    name = 'auth'

    def init_app(self, app):   # Инициируем работу с аутентификацией и авторизацией

        self.extension = Auth(app.web_app, app.db)

    def configurate_extension(self):

        User = self.extension.User
        User.create_table(fail_silently=True)

        if not User.select().where(User.username == 'admin').exists():
            admin = User(username='admin', email='', admin=True, active=True)
            admin.set_password('admin')
            admin.save()
