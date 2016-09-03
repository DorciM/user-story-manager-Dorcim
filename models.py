from peewee import *

db = PostgresqlDatabase('sprintmanager_app', user='doramedgyasszay')

class BaseModel(Model):

    class Meta():
        database = db

class User_story(BaseModel):
    title = CharField()
    story = CharField()
    acceptance_criteria = CharField()
    b_value = FloatField()
    estimation = FloatField()
    status = CharField()

db.connect()

print("Drop table!")
db.drop_tables([User_story], safe=True)

print("Create table!")
db.create_tables([User_story], safe=True)