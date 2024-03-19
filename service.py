import repository




def login_with_email(email, password):
    """
    Function that checks if the email exists in the repository and if the password matches.
    
    Args:
        email (str): The email of the user.
        password (str): The password of the user.
    
    Returns:
        bool or str: If the email exists, it compares the password and returns True if it matches, False otherwise. If the email does not exist, it returns 'User does not exist'
    """
    user = repository.get_user_by_email(email)
    
    if user is None:
        return 'User does not exist'
    
    if user.password == password:
        return user
    else:
        return False


def login_with_username(username, password):
    """
    Function that checks if the username exists in the repository and if the password matches.
    
    Args:
        username (str): The username of the user.
        password (str): The password of the user.
    
    Returns:
        bool or str: If the username exists, it compares the password and returns True if it matches, False otherwise. If the username does not exist, it returns 'User does not exist'
    """
    user = repository.get_user_by_username(username)
    
    if user is None:
        return 'User does not exist'
    
    if user.password == password:
        return user
    else:
        return False


def get_user_learning_trees(user_id):
    """
    Function that retrieves the learning trees a user is assigned to based on their user id
    
    Args:
        user_id (int): The id of the user
    
    Returns:
        list: A list of learning trees the user is assigned to
    """
    user_learning_trees = repository.get_user_learning_trees(user_id)
    if len(user_learning_trees) == 0:
        return None
    else:
        return user_learning_trees
    



def get_lessons_by_learning_tree_id(learning_tree_id):
    """
    Function that retrieves the list of lessons from the repository and returns it given the learning tree id
    
    Args:
        learning_tree_id (int): The id of the learning tree
    
    Returns:
        list: A list of lessons associated with the learning tree id
    """
    lessons = repository.get_lessons_by_learning_tree_id(learning_tree_id)
    if len(lessons) == 0:
        return None
    else:
        return lessons




def get_lesson_by_id(lesson_id):
    """
    Function that retrieves a lesson from the repository based on its lesson id
    
    Args:
        lesson_id (int): The id of the lesson
    
    Returns:
        Lesson: The lesson object with the given id, or None if it does not exist
    """
    lesson = repository.get_lesson_by_id(lesson_id)
    if lesson is None:
        return None
    else:
        return lesson




def get_user(user_id):
    """
    Function that retrieves a user from the repository based on its user id
    
    Args:
        user_id (int): The id of the user
    
    Returns:
        User: The user object with the given id, or None if it does not exist
    """
    user = repository.get_user_by_id(user_id)
    if user is None:
        return None
    else:
        return user

