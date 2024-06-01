from peewee import *

db = SqliteDatabase('data.db')


class VehicleEventRecord(Model):
    plateCode = CharField(index=True)
    description = CharField()
    date = CharField()
    dangerLevel = IntegerField()

    class Meta:
        database = db


def create_tables():
    db.create_tables([VehicleEventRecord])


def drop_tables():
    db.drop_tables([VehicleEventRecord])
