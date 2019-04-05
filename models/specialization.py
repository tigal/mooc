from peewee import *

from application import DB


class Specialization(DB.Model):

    spec_id = PrimaryKeyField()
    name = CharField(30, unique=True, null=False)

    class Meta:
        table_name = 'specializations'

    # def __unicode__(self):
    #     return '%s: %s' % (self.category_id, self.name)

    def __str__(self):
        return self.name