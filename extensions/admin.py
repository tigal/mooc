# -*- coding: utf-8 -*-

from flask_peewee.admin import Admin, ModelAdmin

from extensions import InitBaseExtension


class InitAdminDashboard(InitBaseExtension):

    name = 'admin'

    def init_app(self, app):  # Инициируем Админку
        self.extension = Admin(app.web_app, app.auth)

    def configurate_extension(self):

        from ui.admin import get_admin_models

        for m in get_admin_models():
            orm_m, adm_m = m if len(m) == 2 else [m[0], ModelAdmin]
            self.extension.register(orm_m, adm_m)
        self.extension.setup()
