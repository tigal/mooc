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
        return CourseTheme.select(CourseTheme.name).where(CourseTheme.course_id==cls.course_id)

    @classmethod
    def can_get_certificate(cls, student_id):
        student_themes_cnt = StudentFinishedTheme.select().where(StudentFinishedTheme.student_id == student_id &
                                                           StudentFinishedTheme.course_id == cls.course_id).count()
        courses_themes_cnt = cls.get_themes.count()
        if round(student_themes_cnt/courses_themes_cnt) >= cls.certificate_get:
            return True
        return False

    @classmethod
    def get_finished_themes(cls,student_id):
        CourseTheme.select(CourseTheme.name).join(FinishedTheme,
                                                  on=(CourseTheme.theme_id == FinishedTheme.course_id)).where(
            FinishedTheme.student_id == student_id & FinishedTheme.course_id == cls.course_id)

    @classmethod
    def get_certificate(cls, student_id):
        if cls.can_get_certificate(student_id):
            str = "Course name: " + cls.course_name
            courses_themes = course.get_finished_themes(student_id)
            str += "Themes: \n"
            for row in courses_themes:
                str += row["name"] + '\n'
            # create new certificate
            CertificateCourse.insert(student_id=student_id, course_id=cls.course_id, text = str)
            print(str)
        else:
            print ('Too less themes passed. Certificate cannot be issued')


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
