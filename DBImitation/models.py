
class User(object):
    def __init__(self, id, username, email, password, level=0, profile_picture=None, token='placeholder token'):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.level = level
        self.profile_picture = profile_picture
        self.token = token
        self.creator = False
        self.admin = False
        self.premium = False
        

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
        


class Lesson(object):
    def __init__(self, id, learning_tree_id, lesson_requirements_id, title, description, image):
        self.id = id
        self.learning_tree_id = learning_tree_id
        self.lesson_requirements_id = lesson_requirements_id
        self.title = title
        self.description = description
        self.image = image


class LessonRequirement(object):
    def __init__(self, id, lesson_id1=None, lesson_id2=None, lesson_id3=None, learning_tree_id1=None, learning_tree_id2=None):
        self.id = id
        self.lesson_id1 = lesson_id1
        self.lesson_id2 = lesson_id2
        self.lesson_id3 = lesson_id3
        self.learning_tree_id1 = learning_tree_id1
        self.learning_tree_id2 = learning_tree_id2


class Achievement(object):
    def __init__(self, id, name, description, icon, achievement_requirement_id):
        self.id = id
        self.name = name
        self.description = description
        self.icon = icon
        self.requirement_id = achievement_requirement_id

class UserAchievement(object):
    def __init__(self, id, user_id, achievement_id):
        self.id = id
        self.user_id = user_id
        self.achievement_id = achievement_id



class AchievementRequirement(object):
    """
    Represents the requirement for an achievement, 
    it will have a unique id and a list of ids of required achievements
    """
    def __init__(self, id, lesson_id1=None, lesson_id2=None, lesson_id3=None, learning_tree_id1=None, learning_tree_id2=None):
        self.id = id
        self.lesson_id1 = lesson_id1
        self.lesson_id2 = lesson_id2
        self.lesson_id3 = lesson_id3
        self.learning_tree_id1 = learning_tree_id1
        self.learning_tree_id2 = learning_tree_id2
