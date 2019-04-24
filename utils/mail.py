# -*- coding: utf-8 -*-

from flask import current_app as app

import smtplib
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate


class MailSendingError(Exception):
    msg = 'Ошибка отправки письма'

    def __init__(self, exc):
        print(exc)
        self.exc = exc


def create_message(to, subject, alternative=False):
    msg = MIMEMultipart()
    from_add = f'"{app.config["SMTP_FROM_SYS_NAME"]}" <{app.config["SMTP_FROM"]}>'
    msg['Subject'] = subject
    msg['Date'] = formatdate(localtime=True)
    msg['From'] = from_add
    msg['Reply-To'] = from_add
    msg['To'] = to
    return msg


def send_message(to, msg):

    try:
        smtp = smtplib.SMTP(app.config['SMTP_SERVER'], app.config['SMTP_PORT'])
        smtp.sendmail(app.config['SMTP_FROM'], to, msg.encode('utf-8'))
    except Exception as exc:
        if isinstance(exc, smtplib.SMTPRecipientsRefused):
            for r in exc.recipients:
                app.logger.info('mail address refused: %s, %s' % (r, exc.recipients[r]))
        else:
            app.logger.info('send message error: %s', to)
        raise MailSendingError(exc=exc)
    else:
        smtp.quit()
