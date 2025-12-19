from peewee import Model, ForeignKeyField, DateTimeField, IntegerField
from .db import db
from .user import User
from .product import Product
from .review import Review
from peewee import IntegerField

class Order(Model):
    user = ForeignKeyField(User, backref='orders')
    product = ForeignKeyField(Product, backref='orders')
    quantity = IntegerField()
    order_date = DateTimeField()
    quantity = IntegerField(default=1)
    review = ForeignKeyField(Review, backref='orders', null=True)

    class Meta:
        database = db
