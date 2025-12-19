from peewee import Model, CharField, IntegerField
from .db import db

class User(Model):
    name = CharField()
    age = IntegerField()
    address = CharField()
    class Meta:
        database = db

    @staticmethod
    def get_age_distribution():
        """年代別のユーザー数を取得"""
        users = User.select()
        distribution = {
            '10代': 0, '20代': 0, '30代': 0, '40代': 0,
            '50代': 0, '60代以上': 0
        }

        for user in users:
            if user.age < 20:
                distribution['10代'] += 1
            elif user.age < 30:
                distribution['20代'] += 1
            elif user.age < 40:
                distribution['30代'] += 1
            elif user.age < 50:
                distribution['40代'] += 1
            elif user.age < 60:
                distribution['50代'] += 1
            else:
                distribution['60代以上'] += 1

        return [
            {'label': k, 'value': v}
            for k, v in distribution.items()
        ]
