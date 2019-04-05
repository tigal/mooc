# Written by Galya
# -*- coding: utf-8 -*-

from models.student import Student
from models.course import Course, CourseTheme, Question
from models.user_defined import UserDefinedCourse, UserDefinedTheme
from models.student_answers import StudentAnswerQuestion,StudentFinishedTheme
from models.provider import Provider
from models.specialization import Specialization
from models.schedule import Schedule
from models.certificate import CertificateCourse, CertificateSpec
from application import DB


def clean_student():
    DB.database.execute_sql('delete from students')


def clean_course():
    DB.database.execute_sql('delete from courses')


def clean_certificate_course():
    DB.database.execute_sql('delete from certificate_course')


def clean_certificate_spec():
        DB.database.execute_sql('delete from certificate_spec')


def clean_provider():
    DB.database.execute_sql('delete from providers')


def clean_question():
    DB.database.execute_sql('delete from questions')


def clean_schedule():
    DB.database.execute_sql('delete from schedule')


def clean_specializations():
    DB.database.execute_sql('delete from specializations')


def clean_student_answers():
    DB.database.execute_sql('delete from student_answers')


def clean_student_answers_test_q():
    DB.database.execute_sql('delete from student_answers_test_q')


def clean_student_fin_courses():
    DB.database.execute_sql('delete from student_fin_courses')


def clean_student_fin_tests():
    DB.database.execute_sql('delete from student_fin_tests')


def clean_student_fin_themes():
    DB.database.execute_sql('delete from student_fin_themes')


def clean_test_questions():
    DB.database.execute_sql('delete from test_questions')


def clean_tests():
    DB.database.execute_sql('delete from tests')


def clean_themes():
    DB.database.execute_sql('delete from themes')


def clean_ud_courses():
    DB.database.execute_sql('delete from ud_courses')


def clean_ud_themes():
    DB.database.execute_sql('delete from ud_themes')


def clean_tables():
    clean_student()
    clean_tables()
    clean_certificate_course()
    clean_certificate_spec()
    clean_course()
    clean_provider()
    clean_question()
    clean_schedule()
    clean_specializations()
    clean_student_answers()
    clean_student_answers_test_q()
    clean_student_fin_courses()
    clean_student_fin_tests()
    clean_student_fin_themes()
    clean_test_questions()
    clean_tests()
    clean_themes()
    clean_ud_courses()
    clean_ud_themes()


clean_tables()
print("Tables cleaned")

