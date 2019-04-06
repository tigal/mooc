from datetime import datetime
from peewee import *

from application import DB
from models.course import Course


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

    def get_certificate(self):
        if self.certs.select().where(): st id = course id
            print('get cert')
        else:
            print('not')
        # Course.get_themes(DB.database.execute_sql(
        #     'select course_id from certificate_course, students where self.student_id = certificate_course.student_id'))


