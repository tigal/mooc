from datetime import datetime
from peewee import *

from application import APP


class Student(APP.db.Model):

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

    @classmethod
    def get_certificate_list(cls):
        cert_list = APP.db.database.CertificateCourse.select().where(cls.student_id == APP.db.database.CertificateCourse.student_id)
        for row in cert_list:
            print(row["text"])
