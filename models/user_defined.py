
from datetime import datetime
from peewee import *

from application import APP
from models.specialization import Specialization
from models.student import Student
from models.course import CourseTheme

cert_get_value= 0.6


class UserDefinedCourse(APP.db.Model):
    ud_course_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field='student_id', null=False)
    spec_id = ForeignKeyField(Specialization, to_field='spec_id', null=False)
    creation_date = DateTimeField(default=datetime.now, null=False)
    points = IntegerField(default=0, null=False)
    certificate_get = cert_get_value

    class Meta:
        table_name = 'ud_courses'

    def __str__(self):
        return self.name


class UserDefinedTheme(APP.db.Model):
    ud_theme_id = PrimaryKeyField()
    ud_course_id = ForeignKeyField(UserDefinedCourse, to_field='ud_course_id', on_delete='CASCADE', null=False)
    theme_id = ForeignKeyField(CourseTheme, to_field='theme_id', null=False)

    class Meta:
        table_name = 'ud_themes'

    def __str__(self):
        return self.name