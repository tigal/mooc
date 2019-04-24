# -*- coding: utf-8 -*-

from behave import given,when,then
from models.course import CertificateCourse
from models.student import Student


@given('student with id 1234 requests certificate for course_id 2')
def certificate_requested(context):
    context.certificate = CertificateCourse.create(student_id = 1234, course_id = 2, text = '')
    context.certificate.set_status('requested')


@given('there is no verified userdata in DB')
def check_user_in_DB(context):
    Student.update(verified = False).where(Student.student_id == context.certificate.student_id)
    context.certificate.set_status('verified')


@given('there is verified userdata in DB')
def check_user_in_DB(context):
    context.certificate.set_status('verified')


@given('student with id 1234 requests certificate with id 9876')
def certificate_requested(context):
    try:
        context.certificate = CertificateCourse.get(CertificateCourse.cert_id == 9876)
    except CertificateCourse.DoesNotExist:
        context.certificate = CertificateCourse.create(student_id=1234, course_id=2, text='')
    context.certificate.set_status('requested')
        

@given('certificate is expired')
def set_status_expired(context):
    context.certificate.set_status('expired')


@when('system verifies userdata for certificate')
def verify_user(context):
    pass


@when('system checks certificate in DB')
def certificate_existence_check(context):
    context.certificate_exists = True


@then('there is an error that userdata should be verified')
def print_error_verification(context):
    print(context.certificate.cert_status)
    print('Userdata should be verified')


@then('status of certificate is "refused"')
def set_status_refused(context):
    context.certificate.set_status('refused')
    print(context.certificate.cert_status)


@then('status of certificate is "user_verified"')
def set_status_verified(context):
    print(context.certificate.cert_status)


@then('status of certificate is "updated"')
def set_status_updated(context):
    context.certificate.set_status('updated')
    print(context.certificate.cert_status)


@then('system replaces old certificate')
def replace_certificate(context):
    pass
