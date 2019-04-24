# -*- coding: utf-8 -*-

import os
from datetime import datetime
from shutil import copyfile
from log import add_loggers


if __name__ == '__main__':

    from application import APP
    log = APP.web_app.logger
    add_loggers(APP)

    if not os.path.isfile('local_settings.py.tmpl'):
        err_txt = 'Отсутствует шаблон локального файла настроек.'
        log.error(err_txt)
        raise FileNotFoundError(err_txt)
    else:

        try:
            import local_settings
        except ImportError:
            copyfile('local_settings.py.tmpl', 'local_settings.py')
            log.warning('Отсутствует локальный файл настроек. Файл создан из шаблона local_settings.py.tmpl')

        try:
            log.info('Launched: application %s' % datetime.now())

            APP(local_settings)
            APP.init_extensions()  # Иницализируем расширения
            APP.web_app.run()  # Запускаем приложение

        except Exception as e:
            log.error(e)
