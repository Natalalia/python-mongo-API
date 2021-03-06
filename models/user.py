import mongoengine

class User(mongoengine.Document):
    username = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'userApi',
        'collection': 'users'
    }