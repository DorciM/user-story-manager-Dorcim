from models import *

db.connect()

print("Drop table!")
db.drop_tables([User_story], safe=True)

print("Create table!")
db.create_tables([User_story], safe=True)