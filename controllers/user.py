from models.user import User

def add_user(username) -> User:
    user = User()
    user.username = username
    user.save()

    return user