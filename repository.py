from DBImitation.models import User, LearningTree, UserLearningTree, Lesson


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
        

def get_user_learning_trees(user_id):
    user_learning_trees = []
    for user_learning_tree in DummyRepository().user_learning_trees:
        if user_learning_tree.user_id == user_id:
            user_learning_trees.append(DummyRepository().learning_trees[user_learning_tree.learning_tree_id-1])
    return user_learning_trees


def get_lessons_by_learning_tree_id(learning_tree_id):
    lessons = []
    for lesson in DummyRepository().lessons:
        if lesson.learning_tree_id == learning_tree_id:
            lessons.append(lesson)
    return lessons



class DummyRepository:
    def __init__(self):
        self.users = [
            User(1, "test", "test@example.com", 'test'),
            User(2, "doe", "doe@example.com",'doe')
        ]
        
        self.learning_trees = [
            LearningTree(1, "FirstLearningTree", "This is the first learning tree description placeholder", "no image so far"),
            LearningTree(2, "SecondLearningTree", "This is the second learning tree description placeholder", "no image so far"),
        ]
        
        self.user_learning_trees = [
            UserLearningTree(1, 1, 1),
            UserLearningTree(2, 1, 2),
        ]
        
        self.lessons = [
            Lesson(id=1, learning_tree_id=1, title="Lesson 1", description="Introduction to Python basics", image="lesson1_image.jpg"),
            Lesson(id=2, learning_tree_id=1, title="Lesson 2", description="Data types and variables", image="lesson2_image.jpg"),
            Lesson(id=3, learning_tree_id=1, title="Lesson 3", description="Control flow and loops", image="lesson3_image.jpg"),
            Lesson(id=4, learning_tree_id=1, title="Lesson 4", description="Functions and modules", image="lesson4_image.jpg"),
            Lesson(id=5, learning_tree_id=1, title="Lesson 5", description="Advanced topics", image="lesson5_image.jpg"),
        ]