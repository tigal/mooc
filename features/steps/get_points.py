# -*- coding: utf-8 -*-

from behave import given, when, then
from models.course import CourseTheme
from models.student_answers import StudentAnswerQuestion
from peewee import fn


@given('a set of themes in course')
def step_impl(context):
    for row in context.table:
        try:
            CourseTheme.get(CourseTheme.name == row['name'])
        except CourseTheme.DoesNotExist:
            CourseTheme.create(name=row['name'],
                               max_points=row['max_points'])

@given('a set of student answers')
def step_impl(context):
    for row in context.table:
        try:
            StudentAnswerQuestion.get(StudentAnswerQuestion.student_id == row['student_id'])
        except StudentAnswerQuestion.DoesNotExist:
            StudentAnswerQuestion.create(student_id=row['student_id'],
                                   theme_id=row['theme_id'],
                                   points=row['points'])

@when('we want to know 4545 students points in Pandas')
def step_impl(context):
    name1 = 4545
    name2 = "Pandas"
    try:
        context.result = StudentAnswerQuestion.select(fn.SUM(StudentAnswerQuestion.points).alias('total')).join(CourseTheme,
                           on=(StudentAnswerQuestion.theme_id == CourseTheme.theme_id)).where(StudentAnswerQuestion.student_id == name1 &
                                                                                          CourseTheme.name == name2).group_by(StudentAnswerQuestion.student_id)
    except StudentAnswerQuestion.DoesNotExist:
        context.result = None
    assert context.result is not None

@then('we get {sum:d}')
def step_impl(context, sum):
    assert context.result == sum

