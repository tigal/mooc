from datetime import datetime
from peewee import *

from application import DB


class Provider(DB.Model):

    provider_id = PrimaryKeyField()
    name = CharField(50, null=False)
    email = CharField(30, default="no")
    phone = CharField(21, default="no")
    creation_date = DateTimeField(default=datetime.now, null=False)

    class Meta:
        table_name = 'providers'

    def __unicode__(self):
        return '%s %s' % (self.provider_id, self.name)

    def __str__(self):
        return '%s %s' % (self.provider_id, self.name)