# -*- coding: utf-8 -*-

from behave import given, when, then
from models.quick_tests import Test

@given('I passed Python skill confirmation test with "{percent}" of correct answers')
def positive_test_completion(context, percent):
    context.test_progress_status = context.active_outline[0]
    print(context.test_progress_status)


@given('certificate can be generated if "{max_points}" of a test questions are answered correctly')
def certificate_generating_constant(context, max_points):
    #get row with name Python, get its cerificate_get value
    context.certificate_generating_percent = Test.certificate_get


@when("I want to get the certificate")
def clicking_certificate_generation(context):
    context.request_certificate_generation = True


@then('the system generates a certificate about confirmed skills with the test name and mark "{percent}"')
def successful_generating(context, percent):
    certificate_generation = False
    if (context.test_progress_status >= context.certificate_generating_percent) and context.request_certificate_generation:
        certificate_generation = True
    if certificate_generation:
        print('ok')
