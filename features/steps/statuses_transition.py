# -*- coding: utf-8 -*-

from application import DB
from behave import given,when,then
from models.certificate import CertificateCourse
from models.student import Student


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

@given('certificate is requested')
def certificate_requested(context):
    context.request_certificate_generation = True
    context.certificate = ''

@given('there are no verified userdata in DB')
def check_user_in_DB(context):
    context.is_verified = False

@given('there are verified userdata in DB')
def check_user_in_DB(context):
    context.is_verified = False
    if Student.get(Student.is_verified):
        context.is_verified = True

@when('system verifies userdata for certificate')
def verify_user(context):
    if context.is_verified:
        context.user_verified = True

@then('there is an error that userdata should be verified')
def print_error_verification(context):
    if not context.user_verified:
        print('Userdata should be verified')

@then('status of certificate is "refused"')
def set_status_refused(context):
    context.certificate.set_status('updated')

@then('status of certificate is "userdata verified"')
def set_status_verified(context):
    context.certificate.set_status('user verified')

@given('certificate is expired')
def set_status_expired(context):
    context.certificate.set_status('expired')