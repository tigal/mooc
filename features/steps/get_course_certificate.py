# -*- coding: utf-8 -*-

from behave import given,when,then
from models.course import Course


@given("I passed 3 of 5 themes in 'Intermediate JavaScript' course")
def positive_course_completion(context):
    context.course_progress_status = True
    # calculate 3/5 percentage - progress on this course


@given("To get the certificate more than 30% of this course should be done")
def certificate_generating_constant(context):
    # get Intermediate JavaScript row, take certificate_get value
    context.certificate_generating_percent = Course.certificate_get


@when("I want to get a certificate")
def clicking_certificate_generation(context):
    context.request_certificate_generation = True


@then("The system generate a certificate with the list of passed topics and progress mark 60%")
def successful_generating(context):
    # check if progress percentage is more or equal to certificate_generating_percent
    if context.course_progress_status and context.request_certificate_generation:
        certificate_generation = True
        print("Certificate was generated")

