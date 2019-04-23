# -*- coding: utf-8 -*-

from application import DB
from behave import given,when,then
from models.certificate import CertificateCourse

@given('student with id 1234 requests certificate with id 9876')
def certificate_requested(context):
    context.request_certificate_generation = True

@given('there is existing certificate for student 1234 with id 9876 in DB')
def certificate_in_db(context):
    try:
        context.old_certificate = CertificateCourse.get(CertificateCourse.cert_id.where
                                                    (CertificateCourse.cert_id == '9876' and
                                                     CertificateCourse.student_id == '1234'))
    except CertificateCourse.DoesNotExist:
        CertificateCourse.create(cert_id='9876', student_id = '1234')

@when('system checks certificate in DB')
def certificate_existence_check(context):
    context.certificate_exists = True


@then('status of certificate is "updated"')
def set_status_updated(context):
    context.old_certificate.set_status('updated')

@then('system replaces old certificate')
def replace_certificate(context):
    context.old_certificate = context.new_certificate