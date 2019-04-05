# Written by Galya

# -*- coding: utf-8 -*-
from models.student_answers import StudentFinishedTheme,StudentFinishedTest
from models.course import Course
from models.user_defined import UserDefinedCourse
from models.quick_tests import Test


# User story 1
def student_can_get_certificate(student_id, course_id, ud_course_id):

    if ud_course_id:
        student_perc = StudentFinishedTheme.select().where(StudentFinishedTheme.student_id == student_id &
                                                           StudentFinishedTheme.us_course_id == ud_course_id).count()
        needed_perc = Course.select(Course.certificate_get).where(UserDefinedCourse.ud_course_id == ud_course_id).certificate_get
    else:
        student_perc = StudentFinishedTheme.select().where(StudentFinishedTheme.student_id == student_id &
                                                           StudentFinishedTheme.course_id == course_id).count()
        needed_perc = Course.select(Course.certificate_get).where(Course.course_id == course_id).certificate_get

    if student_perc >= needed_perc:
        return True
    return False


# User story 2
def student_can_get_certificate_quick_test(student_id, test_id):

    student_perc = StudentFinishedTest.select().where(StudentFinishedTest.student_id == student_id &
                                                       StudentFinishedTest.test_id == test_id).count()
    needed_perc = Test.select(Test.certificate_get).where(Test.test_id == test_id).certificate_get
    if student_perc >= needed_perc:
        return True
    return False
