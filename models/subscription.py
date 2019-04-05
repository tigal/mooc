from datetime import datetime
from peewee import *

from application import DB
from models.student import Student
from models.course import Course
from models.user_defined import UserDefinedCourse


class Subscription(DB.Model):
    sub_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field='student_id', null=False)
    course_id = ForeignKeyField(Course, to_field='course_id', default=None)
    ud_course_id = ForeignKeyField(UserDefinedCourse, to_field='ud_course_id',default=None)
    start_date = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)

    class Meta:
        table_name = 'subscriptions'