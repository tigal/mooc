from behave import given,when,then
from models.course import CertificateCourse
from models.student import Student


@given('student with id 1234 requests certificate for course_id 2')
def certificate_requested(context):
    context.certificate = CertificateCourse.create(student_id = 1234, course_id = 2, text = '')
    context.certificate.set_status('requested')


@given('student has points less than needed in this course')
def check_users_points(context):
    Student.update(verified = False).where(Student.student_id == context.certificate.student_id)
    context.certificate.set_status('verified')


@given('student has points more or equal than needed in this course')
def check_users_points(context):
    context.certificate.set_status('verified')


@when('system verifies userdata for certificate')
def verify_user(context):
    pass


@then('there is an error that there are not enough points')
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
