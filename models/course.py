from datetime import datetime
from peewee import *

from application import DB
from models.specialization import Specialization
from models.provider import Provider

cert_get_value= 0.3


class Course(DB.Model):
    course_id = PrimaryKeyField()
    name = CharField(100, null=False)
    provider = ForeignKeyField(Provider, to_field='provider_id')
    spec = ForeignKeyField(Specialization, to_field= 'spec_id')
    creation_date = DateTimeField(default=datetime.now, null=False)
    points = IntegerField(default=0, null=False)
    certificate_get = cert_get_value

    class Meta:
        table_name = 'courses'

    def __str__(self):
        return self.name

    @classmethod
    def get_themes(cls):
        DB.database.execute_sql(
            'select count(*) from themes, courses where courses.course_id = themes.course_id and courses.name = self.name group by course_id').fetchone()


class CourseTheme(DB.Model):
    theme_id = PrimaryKeyField()
    course_id = ForeignKeyField(Course, to_field= 'course_id', backref='themes')
    name = CharField(100, null=False)
    points = IntegerField(default=0, null=False)


    class Meta:
        table_name = 'themes'

    def __str__(self):
        return self.name


class Question(DB.Model):
    question_id = PrimaryKeyField()
    theme_id = ForeignKeyField(CourseTheme, to_field= 'theme_id')
    description = CharField(300, null=False)
    max_points = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'questions'

    def __str__(self):
        return self.name