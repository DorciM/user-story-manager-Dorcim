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
