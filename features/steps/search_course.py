# -*- coding: utf-8 -*-

from behave import given, when, then
from models.course import Course
from models.specialization import Specialization
from models.provider import Provider


@given('a set of specializations')
def step_impl(context):
    for row in context.table:
        Specialization.get_or_create(name=row['name'])


@given('a set of providers')
def step_impl(context):
    for row in context.table:
        Provider.get_or_create(name=row['name'])


@given('a set of courses')
def step_impl(context):
    for row in context.table:
        try:
            Course.get(Course.name == row['name'])
        except Course.DoesNotExist:
            Course.create(name=row['name'],
                          provider_id=row['provider_id'],
                          spec_id=row['spec_id'])


@when('we search for courses in "{name}"')
def step_impl(context, name):
    try:
        context.result = Specialization.select(name).join(Course, on=(Specialization.spec_id == Course.spec_id)).where(Specialization.name == name)
    except Specialization.DoesNotExist:
        context.result = None
    assert context.result is not None


@then('we will find {count:d} Programming items')
def step_impl(context, count):
    assert context.result.count() == count
