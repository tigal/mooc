# -*- coding: utf-8 -*-

from application import DB
from behave import given,when,then
from models.certificate import CertificateCourse

@given('certificate is requested')
def certificate_requested(context):
    context.request_certificate_generation = True

@given('there is existing certificate in DB')
def certificate_in_db(context):
    context.old_certificate = CertificateCourse.get(CertificateCourse.cert_id.where
                                                (CertificateCourse.course_id == context.course_id and
                                                 CertificateCourse.student_id == context.student_id))

@when('system checks certificate in DB')
def certificate_existence_check(context):
    context.old_certificate = True


@then('status of certificate is "updated"')
def set_status_updated(context):
    CertificateCourse.set_status('updated')

@then('system replaces old certificate')
def replace_certificate(context):
    pass