from behave import given,when,then
from models.course import CertificateCourse
from models.student import Student


@given('student has points less than needed in this course')
def check_users_points(context):
    Student.update(verified = False).where(Student.student_id == context.certificate.student_id)
    context.certificate.set_status('verified')


@given('student has points more or equal than needed in this course')
def check_users_points(context):
    context.certificate.set_status('verified')


@then('there is an error that there is not enough points')
def print_error_verification(context):
    print(context.certificate.cert_status)
    print('There are not enough points')


@then('status of certificate is "refused"')
def set_status_refused(context):
    context.certificate.set_status('refused')
    print(context.certificate.cert_status)


@then('status of certificate is "generated"')
def set_status_updated(context):
    context.certificate.set_status('updated')
    print(context.certificate.cert_status)
