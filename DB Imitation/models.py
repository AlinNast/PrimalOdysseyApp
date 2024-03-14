
class User(object):
    def __init__(self, id, username, email, password, level=0, profile_picture=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.level = level
        self.profile_picture = profile_picture
