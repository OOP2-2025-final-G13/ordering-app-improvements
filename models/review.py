from peewee import Model, IntegerField, TextField
from .db import db 

class Review(Model):
    rating = IntegerField()
    comment = TextField()

    class Meta:
        database = db