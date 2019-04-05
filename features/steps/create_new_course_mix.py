# -*- coding: utf-8 -*-

from behave import given, when, then
from models.course import Course

user_selected_themes_r = ["R and Data Science. Introduction",
                         "R and Data Science. Intermediate"]
courses = []


@given("there is a Python course")
def given_python_course(context):
    for row in context.table:
        courses.append(row['course'])
    print(courses)


@given("there is an R course that includes data scienсe lessons I want to learn")
def set_course(context):
    # print(user_selected_themes_r)
    context.wanted_themes = []


@when("I choose topics from R course to add to Python course")
def choosing_course_topics(context):
    pass
    # find in CourseTheme themes from user_selected_themes_r
    # save in context.r_themes


@then("the system creates a new course")
def create_user_course(context):
    pass
    # create new UserCreatedCourse, save it in context.new_course


@then("the system adds selected topics from Python course to the new course")
def add_themes_from_python(context):
    pass
    # find Python course in Course table
    # select Python themes from Theme table
    # add Python themes in UserCreatedTheme with link on context.new_course


@then("the system adds selected topics from R course to new course")
def add_themes_from_course(context):
    # for i in context.r_themes:
    # insert i theme in UserCreatedTheme table with link on context.new_course
    themes = []
    for theme in context.wanted_themes:
        themes.append(theme)

