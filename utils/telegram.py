# -*- coding: utf-8 -*-

import requests
from flask import current_app as app


class BotHandler(object):

    api_url = None

    def make_url(self):
        if self.api_url is None:
            self.api_url = app.config['TELEGRAM_BOT_URL']

    def get_updates(self, offset=None, timeout=30):
        self.make_url()
        params = {'timeout': timeout,
                  'offset': offset}
        try:
            resp = requests.get(self.api_url + 'getUpdates', params)
            result_json = resp.json()['result']
        except Exception as ex:
            raise
        return result_json

    def send_message(self, chat_id, text):
        self.make_url()
        params = {'chat_id': chat_id,
                  'text': text}
        resp = requests.post(self.api_url + 'sendMessage', params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update


telegram_bot = BotHandler()
