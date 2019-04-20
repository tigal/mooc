from datetime import datetime
from peewee import *

from application import DB
from models.student import Student
from models.specialization import Specialization


class CertificateCourse(DB.Model):
    cert_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field='student_id', null=False, backref='certs')
    course_id = IntegerField(default=0, null=False)
    ud_course_id = IntegerField(default=0, null=False)
    text = CharField(10000)
    issued = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)

    class Meta:
        table_name = 'certificate_course'



class CertificateSpec(DB.Model):
    cert_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field='student_id', null=False)
    spec_id = ForeignKeyField(Specialization, to_field='spec_id',null=False)
    text = CharField(10000)
    issued = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)

    class Meta:
        table_name = 'certificate_spec'