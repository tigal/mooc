# -*- coding: utf-8 -*-

from application import DB
from behave import given,when,then


@given('I passed "{pas}" themes in "Intermediate JavaScript" course')
def positive_course_completion(context, pas):
    # calculate 3/5 percentage - progress on this course
    res = DB.database.execute_sql('select count(*) from themes,courses where courses.course_id = themes.course_id and courses.name = "Intermediate JavaScript" group by course_id').fetchone()
    if res[0] != 0:
        context.user_progress = pas/res[0]
    else:
        context.user_progress = 0


@given("To get the certificate more than 30% of this course should be done")
def certificate_generating_constant(context):
    # get Intermediate JavaScript row, take certificate_get value
    res = DB.database.execute_sql('select certificate_get from courses where name = "Intermediate JavaScript"').fetchone()
    context.certificate_generating_percent = res[0]


@when("I want to get a certificate")
def clicking_certificate_generation(context):
    context.request_certificate_generation = True


@then("The system generate a certificate with the list of passed topics and progress mark 60%")
def successful_generating(context):
    # check if progress percentage is more or equal to certificate_generating_percent
    if context.user_progress >= context.certificate_generating_percent and context.request_certificate_generation:
        print("Certificate was generated")

