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
        return user.token
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
        return user.token
    else:
        return False
