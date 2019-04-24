# -*- coding: utf-8 -*-

from behave import given,when,then
from models.course import Course,CourseTheme
from models.student_answers import StudentFinishedTheme


@given('Intermediate JavaScript course themes')
def interm_js_themes(context):
    #create course
    try:
        context.course = Course.get(Course.name.where(Course.name == 'Intermediate JavaScript'))
    except Course.DoesNotExist:
        Course.create(course_name='Intermediate JavaScript')
        context.course = Course.select().where(Course.name == 'Intermediate JavaScript')
    context.student_id = 1
    #create themes
    try:
        context.themes_list = context.course.get_themes()
    except CourseTheme.DoesNotExist:
        for row in context.table:
            CourseTheme.create(course_id=row['course_id'],
                               name=row['name'],
                               points=row['points'])

@given('I passed 3 themes in Intermediate JavaScript course')
def positive_course_completion(context):
    #save finished_themes
    try:
        context.themes_list = context.course.get_finished_themes(1)
    except StudentFinishedTheme.DoesNotExist:
        for row in context.table:
            StudentFinishedTheme.create(student_id=1,
                                        course_id=row['course_id'],
                                        theme_id=row['theme_id'],
                                        points=row['points'])


@given("To get the certificate more than 30% of this course should be done")
def certificate_generating_constant(context):
    # get Intermediate JavaScript row, take certificate_get value
    context.certificate_generating_percent = context.course.get_certificate


@when("I want to get a certificate")
def clicking_certificate_generation(context):
    context.request_certificate_generation = True


@then("The system generate a certificate with the list of passed topics and progress mark 60%")
def successful_generating(context):
    # check if progress percentage is more or equal to certificate_generating_percent
    if context.request_certificate_generation and context.course.get_certificate(context.student_id):
        print("Certificate was generated")

