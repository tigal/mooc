# -*- coding: utf-8 -*-

from behave import given, when, then
from models.course import CourseTheme


@given("there is course that includes both JS-basics and Vue.js themes")
def get_set_themes(context):
    context.themes_set = []
    # context.themes_set = ['Closures', 'Redux', 'Vuex', 'Vue-router']
    context.tabelle = context.table
    for row in context.table:
        context.themes_set.append(row['name'])  # Course_themes.name
    # get courses themes


@given("I want to learn Vue.js only")
def vj_only(context):
    pass


@given("total sum of points must be more than 50 to form a course")
def form_course(context):
    pass


@given("on Vue.js themes 50 points can be got")
def vj_points(context):
    pass


@when("I remove JS-basics themes from this course")
def remove_themes(context):
    context.themes_to_remove = []
    for th in context.themes_set:
        if 'Vue' not in th:
            context.themes_to_remove.append(th)
    print(context.themes_to_remove)


@then("the system creates a new course with Vue.js themes only")
def generate_set_themes(context):
    context.wanted_set = [x for x in context.themes_set if x not in context.themes_to_remove]
    print(context.wanted_set)
    # create new UserDefinedCourse
    # add themes in UserCreatedThemes with link on this course
    # recount points - write separate method
    sum_of_points = 0
    for theme in context.wanted_set:
        sum_of_points += CourseTheme.get(CourseTheme.name == theme).points
    print(sum_of_points)


