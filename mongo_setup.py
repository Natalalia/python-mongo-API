import mongoengine

def global_init():
    mongoengine.register_connection(alias='userApi', name='userApiTest')