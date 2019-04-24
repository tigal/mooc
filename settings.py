# -*- coding: utf-8 -*-

DEBUG = True

LOG_PATH = 'logs/app.log'

ENCODING = 'utf-8'

TRAILING_SLASH = False

SECRET_KEY = 'Secret'

DB_ENGINE = 'peewee.PostgresqlDatabase'

APP_EXTENSIONS = (
    'extensions.models.InitModels',
    'extensions.auth.InitAuth',
    'extensions.admin.InitAdminDashboard',
    'extensions.routes.InitRoutes',
    'extensions.api_1.InitAPI1',
    # 'extensions.api_2.InitAPI2',
)


SMTP_FROM = 'mail@ls.loc'
SMTP_FROM_SYS_NAME = u'LS'
SMTP_SERVER = 'localhost'
SMTP_PORT = 25
