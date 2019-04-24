# -*- coding: utf-8 -*-


from behave import fixture, use_fixture

from application import APP
from features import test_settings


@fixture
def make_test_app_instance(context, *args, **kwargs):

    APP(test_settings, force_init_web_app=True)
    context.client = APP.web_app.test_client()
    APP.web_app.testing = True
    APP.init_extensions()  # Иницализируем расширения

    with APP.db.database.connection_context():  # Пересозадём таблицы для тестов
        APP.extensions['db'].drop_tables()
        APP.extensions['db'].create_tables()

    yield context.client

    # -- CLEANUP:


# def before_feature(context, feature):
def before_all(context):
    # -- HINT: Recreate a new flask client before each feature is executed.
    context.config.setup_logging()
    use_fixture(make_test_app_instance, context)
