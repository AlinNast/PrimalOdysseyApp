from DBImitation.models import User, LearningTree, UserLearningTree, Lesson, LessonRequirement, Achievement, AchievementRequirement, UserAchievement


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


def get_lesson_by_id(lesson_id):
    for lesson in DummyRepository().lessons:
        if lesson.id == lesson_id:
            return lesson
        
        

def get_user_achievements(user_id):
    user_achievements = []
    for user_achievement in DummyRepository().user_achivements:
        if user_achievement.user_id == user_id:
            user_achievements.append(DummyRepository().achievements[user_achievement.achievement_id-1])
    return user_achievements



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
            Lesson(id=1, learning_tree_id=1,lesson_requirements_id=1, title="Lesson 1", description="Introduction to Python basics", image="lesson1_image.jpg"),
            Lesson(id=2, learning_tree_id=1,lesson_requirements_id=2, title="Lesson 2", description="Data types and variables", image="lesson2_image.jpg"),
            Lesson(id=3, learning_tree_id=1,lesson_requirements_id=3, title="Lesson 3", description="Control flow and loops", image="lesson3_image.jpg"),
            Lesson(id=4, learning_tree_id=1,lesson_requirements_id=4, title="Lesson 4", description="Functions and modules", image="lesson4_image.jpg"),
            Lesson(id=5, learning_tree_id=1,lesson_requirements_id=5, title="Lesson 5", description="Advanced topics", image="lesson5_image.jpg"),
        ]
        
        
        self.lesson_requirements = [
            LessonRequirement(lesson_id=1, required_lesson_id=None),  # no requirement
            LessonRequirement(lesson_id=2, required_lesson_id=None),  # requires Lesson 1
            LessonRequirement(lesson_id=3, required_lesson_id=None),  # requires Lesson 2
            LessonRequirement(lesson_id=4, required_lesson_id=3),  # requires Lesson 3
            LessonRequirement(lesson_id=5, required_lesson_id=4),  # no requirement
        ]

        
        self.achivements = [
            Achievement(id=1, title="Achievement 1", description="This is the first achievement description placeholder", image="achiv1_image.jpg", achievement_requirement_id=1),
            Achievement(id=2, title="Achievement 2", description="This is the second achievement description placeholder", image="achiv2_image.jpg", achievement_requirement_id=2),
            Achievement(id=3, title="Achievement 3", description="This is the third achievement description placeholder", image="achiv3_image.jpg", achievement_requirement_id=3),
        ]

        
        self.achivement_requirements = [
            AchievementRequirement(1),
            AchievementRequirement(2, 1),
            AchievementRequirement(3, 5)
        ]
        
        self.user_achivements = [
            UserAchievement(id=1, user_id=1, achievement_id=1),
        ]
