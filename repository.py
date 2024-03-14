from DBImitation.models import User


def get_user_by_id(id):
    for user in DummyRepository().users:
        if user.id == id:
            return user

def get_user_by_email(email):
    for user in DummyRepository().users:
        if user.email == email:
            return user

def get_user_by_username(username):
    for user in DummyRepository().users:
        if user.username == username:
            return user


class DummyRepository:
    def __init__(self):
        self.users = [
            User(1, "test", "test@example.com", 'test'),
            User(2, "doe", "doe@example.com",'doe')
        ]