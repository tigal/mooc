from datetime import datetime
from peewee import *

from application import APP
from models.course import Course
from models.user_defined import UserDefinedCourse


class Schedule(APP.db.Model):

    sched_id = PrimaryKeyField()
    course_id = ForeignKeyField(Course, to_field='course_id',default=None)
    ud_course_id = ForeignKeyField(UserDefinedCourse, to_field='ud_course_id',default=None)
    start_date = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)


    class Meta:
        table_name = 'schedule'

    def __unicode__(self):
        return '%s %s' % (self.sch_id, self.sch_name)

    def __str__(self):
        return '%s %s' % (self.sch_id, self.sch_name)