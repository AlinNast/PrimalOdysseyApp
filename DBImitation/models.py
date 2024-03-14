
class User(object):
    def __init__(self, id, username, email, password, level=0, profile_picture=None, token='placeholder token'):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.level = level
        self.profile_picture = profile_picture
        self.token = token
        

class LearningTree(object):
    def __init__(self, id, name, description, image):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        

class UserLearningTree(object):
    def __init__(self, id, user_id, learning_tree_id):
        self.id = id
        self.user_id = user_id
        self.learning_tree_id = learning_tree_id
