from datetime import datetime
from peewee import *

from application import APP
from models.specialization import Specialization
from models.provider import Provider

cert_get_value= 0.6


class Test(APP.db.Model):
    test_id = PrimaryKeyField()
    name = CharField(100, null=False)
    provider_id = ForeignKeyField(Provider, to_field='provider_id')
    spec_id = ForeignKeyField(Specialization, to_field= 'spec_id')
    creation_date = DateTimeField(default=datetime.now, null=False)
    points = IntegerField(default=0, null=False)
    certificate_get = cert_get_value

    class Meta:
        table_name = 'tests'

    def __str__(self):
        return self.name


class TestQuestion(APP.db.Model):
    test_question_id = PrimaryKeyField()
    test_id = ForeignKeyField(Test, to_field= 'test_id')
    description = CharField(300, null=False)
    max_points = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'test_questions'

    def __str__(self):
        return self.name
