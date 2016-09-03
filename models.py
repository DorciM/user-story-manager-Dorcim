from peewee import *
import config

db = PostgresqlDatabase(config.dbname, user=config.user)

class BaseModel(Model):

    class Meta():
        database = db

class User_story(BaseModel):
    story_title = CharField()
    content = CharField()
    acceptance_criteria = CharField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()

db.connect()

print("Drop table!")
db.drop_tables([User_story], safe=True)

print("Create table!")
db.create_tables([User_story], safe=True)