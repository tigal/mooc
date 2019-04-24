from datetime import datetime
from peewee import *

from application import APP

from models.student import Student
from models.quick_tests import Test,TestQuestion


class StudentAnswerQuestion(APP.db.Model):

    st_answer_q_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field= 'student_id')
    course_id = IntegerField(default=0, null=False)
    theme_id = IntegerField(default=0, null=False)
    ud_theme_id = IntegerField(default=0, null=False)
    question_id = IntegerField(default=0, null=False)
    points = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'student_answers'


class StudentFinishedTheme(APP.db.Model):

    st_theme_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field= 'student_id')
    course_id = IntegerField(default=0, null=False)
    theme_id = IntegerField(default=0, null=False)
    ud_theme_id = IntegerField(default=0, null=False)
    points = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'student_fin_themes'


class StudentFinishedCourse(APP.db.Model):

    st_theme_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field= 'student_id')
    course_id = IntegerField(default=0, null=False)
    ud_course_id = IntegerField(default=0, null=False)
    points = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'student_fin_courses'


class StudentFinishedTest(APP.db.Model):

    st_test_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field= 'student_id')
    test_id = ForeignKeyField(Test, to_field='test_id')
    points = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'student_fin_tests'


class StudentAnswerTestQuestion(APP.db.Model):

    st_test_q_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field= 'student_id')
    test_id = ForeignKeyField(Test, to_field='test_id')
    test_question_id = ForeignKeyField(TestQuestion, to_field='test_question_id')
    points = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'student_answers_test_q'
