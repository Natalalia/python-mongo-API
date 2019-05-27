from models.user import User
from typing import List


def add_user(username) -> User:
    user = User()
    user.username = username
    user.save()

    return user

def get_users() -> List[User]:
    users = User.objects().all()

    return users
