from datetime import datetime
from peewee import *

from application import DB
from models.course import Course, CourseTheme
from models.subscription import Subscription
from models.student_answers import FinishedTheme
from models.certificate import CertificateCourse


class Student(DB.Model):

    student_id = PrimaryKeyField()
    first_name = CharField(50, null=False)
    last_name = CharField(50, null=False)
    email = CharField(unique=True, null=False)
    phone = CharField(21, unique=True, null=False)
    birthday = DateField(null=True)
    creation_date = DateTimeField(default=datetime.now, null=False)
    is_active = BooleanField(default=True)

    class Meta:
        table_name = 'students'

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)

    def get_certificate(self, course_name):
        course_id = course_id = Subscription.select(Subscription.course_id).join(Course, on=(Subscription.course_id == Course.course_id)).where(Subscription.student_id == self.student_id & Course.name == course_name)
        if student_can_get_certificate(self.student_id, course_id, 0):
            str = "Course name: " + course_name
            courses_themes = CourseTheme.select(CourseTheme.name).join(FinishedTheme, on=(CourseTheme.theme_id == FinishedTheme.course_id)).where(FinishedTheme.student_id == self.student_id & FinishedTheme.course_id == course_id)
            str += "Themes: \n"
            for row in courses_themes:
                str += row["name"] + '\n'
            # create new certificate
            CertificateCourse.insert(student_id=self.student_id, course_id=course_id, text = str)
            print(str)
        else:
            print ('Too less themes passed. Certificate cannot be issued')
